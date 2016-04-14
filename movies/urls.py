from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.base import RedirectView

from movies.forms import MovieForm
from movies.models import Movie, Director
from views import MovieList, MovieCreate, MovieDetail, DirectorList, DirectorCreate, DirectorDetail

urlpatterns = patterns('',
    # Home page
    url(r'^$',
        RedirectView.as_view(url=reverse_lazy('movies:movie_list', kwargs={'extension': 'html'})),
        name='home_page'),

    # List movies: /movies/movies.json
    url(r'^movies\.(?P<extension>(json|xml|html))$',
        MovieList.as_view(),
        name='movie_list'),

    # Movie detail: /movies/movies/1.json
    url(r'^movies/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
        MovieDetail.as_view(),
        name='movie_detail'),

    # Create a movie: /movies/movies/create/
    url(r'^movies/create/$',
        MovieCreate.as_view(),
        name='movie_create'),

    # Edit movie details, ex.: /movies/movies/1/edit/
    url(r'^movies/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Movie,
            template_name='movies/form.html',
            form_class=MovieForm),
        name='movie_edit'),


    # List directors: /movies/directors.json
    url(r'^directors\.(?P<extension>(json|xml|html))$',
        DirectorList.as_view(),
        name='director_list'),

    # Create a director: /movies/directors/create/
    url(r'^directors/create/$',
        DirectorCreate.as_view(),
        name='director_create'),

    # Director detail: /movies/directors/1.json
    url(r'^directors/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
        DirectorDetail.as_view(),
        name='director_detail'),

    # Edit movie details, ex.: /movies/movies/1/edit/
    url(r'^director/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Director,
            template_name='movies/form.html',
            form_class=MovieForm),
        name='director_edit'),

)
