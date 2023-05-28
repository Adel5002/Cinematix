from django.urls import path

from .views import MovieListView, MovieDetailView, AddComment

urlpatterns = [
    path('', MovieListView.as_view(), name='movie_list'),
    path('<slug:slug>/', MovieDetailView.as_view(), name='movie_detail'),
    path('review/<slug:url>/', AddComment.as_view(), name='add_review')

]

