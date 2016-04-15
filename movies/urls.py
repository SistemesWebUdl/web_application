from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.base import RedirectView

from movies.forms import MovieForm, ActorForm, CompanyForm, \
    ActorAddForm, DirectorAddForm, CompanyAddForm, DirectorForm
from movies.models import Movie, Director, Actor, Company
from views import MovieList, MovieCreate, MovieDetail, \
    DirectorList, DirectorCreate, DirectorDetail, ActorList, \
    ActorCreate, ActorDetail, CompanyList, CompanyDetail, CompanyCreate

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

    # Edit director details, ex.: /movies/directors/1/edit/
    url(r'^director/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Director,
            template_name='movies/form.html',
            form_class=DirectorForm),
        name='director_edit'),


    # List actors: /movies/actors.json
    url(r'^actors\.(?P<extension>(json|xml|html))$',
        ActorList.as_view(),
        name='actor_list'),

    # Create a actor: /movies/actors/create/
    url(r'^actors/create/$',
        ActorCreate.as_view(),
        name='actor_create'),

    # Actor detail: /movies/actors/1.json
    url(r'^actors/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
        ActorDetail.as_view(),
        name='actor_detail'),

    # Edit actor details, ex.: /movies/actors/1/edit/
    url(r'^actors/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Actor,
            template_name='movies/form.html',
            form_class=ActorForm),
        name='actor_edit'),


    # List companies: /movies/companies.json
    url(r'^companies\.(?P<extension>(json|xml|html))$',
        CompanyList.as_view(),
        name='company_list'),

    # Create a company: /movies/companies/create/
    url(r'^companies/create/$',
        CompanyCreate.as_view(),
        name='company_create'),

    # Company detail: /movies/companies/1.json
    url(r'^companies/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
        CompanyDetail.as_view(),
        name='company_detail'),

    # Edit companies details, ex.: /movies/companies/1/edit/
    url(r'^companies/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Company,
            template_name='movies/form.html',
            form_class=CompanyForm),
        name='company_edit'),

    # Add actors to movie: /movies/actors/1/add/
    url(r'^actors/(?P<pk>\d+)/add/$',
        UpdateView.as_view(
            model=Movie,
            template_name='movies/form.html',
            form_class=ActorAddForm),
        name='actor_add'),


    # Add directors to movie: /movies/directors/1/add/
    url(r'^directors/(?P<pk>\d+)/add/$',
        UpdateView.as_view(
            model=Movie,
            template_name='movies/form.html',
            form_class=DirectorAddForm),
        name='director_add'),

    # Add companies to movie: /movies/companies/1/add/
    url(r'^companies/(?P<pk>\d+)/add/$',
        UpdateView.as_view(
            model=Movie,
            template_name='movies/form.html',
            form_class=CompanyAddForm),
        name='company_add'),

)
