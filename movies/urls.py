from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.base import RedirectView

from models import Country, Company, Actor, Director, Movie
#from forms import MovieForm, ActorForm
from views import MoviesList, MovieCreate

urlpatterns = patterns('',
    # Home page
    url(r'^$',
        RedirectView.as_view(url=reverse_lazy('movies:movie_list', kwargs={'extension': 'html'})),
        name='home_page'),

    # List restaurants: /myrestaurants/restaurants.json
    url(r'^movies\.(?P<extension>(json|xml|html))$',
        MoviesList.as_view(),
        name='movie_list'),

        # Create a restaurant: /myrestaurants/restaurants/create/
    url(r'^movies/create/$',
        MovieCreate.as_view(),
        name='movie_create'),
)
