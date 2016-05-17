from django.conf.urls import patterns, url, include
from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from django.views.generic.base import RedirectView
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

from movies.forms import MovieForm, ActorForm, CompanyForm, \
    ActorAddForm, DirectorAddForm, CompanyAddForm, DirectorForm, \
    CityForm, CityAddForm, CityDirectorForm, CityActorForm, \
    CityCompanyForm
from movies.models import Movie, Director, Actor, Company, City
from views import MovieList, MovieCreate, MovieDetail, \
    DirectorList, DirectorCreate, DirectorDetail, ActorList, \
    ActorCreate, ActorDetail, CompanyList, CompanyDetail, CompanyCreate, \
    CityList, CityDetail, CityCreate, APIMovieList, APIMovieDetail, APICityList, \
    APICityDetail, APIActorList, APIActorDetail, APICompanyList, APICompanyDetail, \
    APIDirectorList, APIDirectorDetail, UserCreate, \
    MovieDelete, DirectorDelete, ActorDelete, CompanyDelete, CityDelete, \
    LoginRequiredCheckIsOwnerUpdateView

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
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=Movie,
            template_name='movies/form.html',
            form_class=MovieForm),
        name='movie_edit'),

    # Delete a movie, ex: movies/movies/1/delete
    url(r'^movies/(?P<pk>\d+)/delete/$', MovieDelete.as_view(),
        name='movie_delete', ),

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
    url(r'^directors/(?P<pk>\d+)/edit/$',
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=Director,
            template_name='movies/form.html',
            form_class=DirectorForm),
        name='director_edit'),

    # Delete a director, ex: movies/directors/1/delete
    url(r'^directors/(?P<pk>\d+)/delete/$', DirectorDelete.as_view(),
        name='director_delete', ),

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
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=Actor,
            template_name='movies/form.html',
            form_class=ActorForm),
        name='actor_edit'),

    # Delete an actor, ex: movies/actors/1/delete
    url(r'^actors/(?P<pk>\d+)/delete/$', ActorDelete.as_view(),
        name='actor_delete', ),

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
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=Company,
            template_name='movies/form.html',
            form_class=CompanyForm),
        name='company_edit'),

    # Delete a company, ex: movies/companies/1/delete
    url(r'^companies/(?P<pk>\d+)/delete/$', CompanyDelete.as_view(),
        name='company_delete', ),


    # List cities: /movies/cities.json
    url(r'^cities\.(?P<extension>(json|xml|html))$',
        CityList.as_view(),
        name='city_list'),

    # Create a city: /movies/cities/create/
    url(r'^cities/create/$',
        CityCreate.as_view(),
        name='city_create'),

    # City detail: /movies/cities/1.json
    url(r'^cities/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
        CityDetail.as_view(),
        name='city_detail'),

    # Edit cities details, ex.: /movies/cities/1/edit/
    url(r'^cities/(?P<pk>\d+)/edit/$',
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=City,
            template_name='movies/form.html',
            form_class=CityForm),
        name='city_edit'),

    # Delete a city, ex: movies/city/1/delete
    url(r'^cities/(?P<pk>\d+)/delete/$', CityDelete.as_view(),
        name='city_delete'),

    # Add actors to movie: /movies/movies/1/actors/add/
    url(r'^movies/(?P<pk>\d+)/actors/add/$',
        UpdateView.as_view(
            model=Movie,
            template_name='movies/form.html',
            form_class=ActorAddForm),
        name='actor_add'),

    # Add directors to movie: /movies/movies/1/directors/add/
    url(r'^movies/(?P<pk>\d+)/directors/add/$',
        UpdateView.as_view(
            model=Movie,
            template_name='movies/form.html',
            form_class=DirectorAddForm),
        name='director_add'),

    # Add companies to movie: /movies/movies/1/companies/add/
    url(r'^movies/(?P<pk>\d+)/companies/add/$',
        UpdateView.as_view(
            model=Movie,
            template_name='movies/form.html',
            form_class=CompanyAddForm),
        name='company_add'),

    # Add cities to movie: /movies/movies/1/cities/add/
    url(r'^movies/(?P<pk>\d+)/cities/add/$',
        UpdateView.as_view(
            model=Movie,
            template_name='movies/form.html',
            form_class=CityAddForm),
        name='city_add'),

    # Select a city for a director: /movies/directors/1/edit_city
    url(r'^directors/(?P<pk>\d+)/edit_city/$',
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=Director,
            template_name='movies/form.html',
            form_class=CityDirectorForm),
        name='city_director_edit'),

    # Select a city for an actor: /movies/actors/1/edit_city
    url(r'^actors/(?P<pk>\d+)/edit_city/$',
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=Actor,
            template_name='movies/form.html',
            form_class=CityActorForm),
        name='city_actor_edit'),

    # Select a city for an actor: /movies/companies/1/edit_city
    url(r'^companies/(?P<pk>\d+)/edit_city/$',
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=Company,
            template_name='movies/form.html',
            form_class=CityCompanyForm),
        name='city_company_edit'),

    url(r'^accounts/newuser/$', UserCreate.as_view(), name='new_user'),

)

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api', 'json', 'xml'])

urlpatterns += patterns('',
    url(r'^api/', include(DefaultRouter().urls)),
    url(r'^api/movies/$', APIMovieList.as_view(), name='movie-list'),
    url(r'^api/movies/(?P<pk>\d+)/$', APIMovieDetail.as_view(), name='movie-detail'),
    url(r'^api/actors/$', APIActorList.as_view(), name='actor-list'),
    url(r'^api/actors/(?P<pk>\d+)/$', APIActorDetail.as_view(), name='actor-detail'),
    url(r'^api/directors/$', APIDirectorList.as_view(), name='director-list'),
    url(r'^api/directors/(?P<pk>\d+)/$', APIDirectorDetail.as_view(), name='director-detail'),
    url(r'^api/cities/$', APICityList.as_view(), name='city-list'),
    url(r'^api/cities/(?P<pk>\d+)/$', APICityDetail.as_view(), name='city-detail'),
    url(r'^api/companies/$', APICompanyList.as_view(), name='company-list'),
    url(r'^api/companies/(?P<pk>\d+)/$', APICompanyDetail.as_view(), name='company-detail')

)
