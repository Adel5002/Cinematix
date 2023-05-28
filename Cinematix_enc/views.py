from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from .forms import ReviewForm
from .models import Movie, Review


class MovieListView(ListView):
    model = Movie
    template_name = 'movie_list.html'
    context_object_name = 'movies'
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_detail.html'
    context_object_name = 'movies'
    slug_field = 'url'


class AddComment(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'movie_detail'

    def form_valid(self, form):
        if self.request.POST.get('parent', None):
            form.instance.parent_id = int(self.request.POST.get('parent'))
        form.instance.movie = Movie.objects.get(url=self.kwargs['url'])
        comments = form.save(commit=False)
        comments.commentator = self.request.user
        comments.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('movie_detail', kwargs={'slug': self.object.movie.url})




