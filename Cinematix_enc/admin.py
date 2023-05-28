from django.contrib import admin

from .models import Category, Genre, Movie, MovieShots, Actor, RatingStar, Rating, Review


class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('name',)}


class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieShots)
admin.site.register(Actor)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Review)
