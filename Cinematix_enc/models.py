from datetime import date

from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=180)
    description = models.TextField()
    url = models.SlugField(max_length=180, unique=True)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=120)
    age = models.PositiveSmallIntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to='actors')

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=180)
    description = models.TextField()
    url = models.SlugField(max_length=180, unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=120)
    tagline = models.CharField(max_length=120, default='')
    description = models.TextField()
    poster = models.ImageField(upload_to='movies/')
    year = models.PositiveSmallIntegerField(default='2022')
    dateCreation = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=30)
    directors = models.ManyToManyField(Actor, related_name='film_director')
    actors = models.ManyToManyField(Actor, related_name='film_actor')
    genre = models.ManyToManyField(Genre)
    world_premiere = models.DateField(default=date.today)
    budget = models.PositiveIntegerField(default=0, help_text='enter amount in dollars')
    fees_in_usa = models.PositiveIntegerField(
        default=0, help_text='enter amount in dollars'
    )
    fees_in_world = models.PositiveIntegerField(
        default=0, help_text='enter amount in dollars'
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
    )
    url = models.SlugField(max_length=180, unique=True)
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['dateCreation']


class MovieShots(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField(upload_to='movie_shots/')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class RatingStar(models.Model):
    value = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.value


class Rating(models.Model):
    ip = models.CharField(max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CharField)

    def __str__(self):
        return f"{self.star} - {self.movie}"


class Review(models.Model):
    text = models.TextField(max_length=5000)
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, blank=True, null=True
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    commentator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.movie
