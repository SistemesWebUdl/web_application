from django.utils import timezone
from django.core import serializers
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import CreateView

from models import Movie, Director, Actor, Company, Country
from forms import MovieForm, DirectorForm, ActorForm, CompanyForm, CountryForm

class ConnegResponseMixin(TemplateResponseMixin):

    def render_json_object_response(self, objects, **kwargs):
        json_data = serializers.serialize(u"json", objects, **kwargs)
        return HttpResponse(json_data, content_type=u"application/json")

    def render_xml_object_response(self, objects, **kwargs):
        xml_data = serializers.serialize(u"xml", objects, **kwargs)
        return HttpResponse(xml_data, content_type=u"application/xml")

    def render_to_response(self, context, **kwargs):
        if 'extension' in self.kwargs:
            try:
                objects = [self.object]
            except AttributeError:
                objects = self.object_list
            if self.kwargs['extension'] == 'json':
                return self.render_json_object_response(objects=objects)
            elif self.kwargs['extension'] == 'xml':
                return self.render_xml_object_response(objects=objects)
        return super(ConnegResponseMixin, self).render_to_response(context)


class MovieList(ListView, ConnegResponseMixin):
    model = Movie
    context_object_name = 'latest_movie_list'
    template_name = 'movies/movie_list.html'


class DirectorList(ListView, ConnegResponseMixin):
    model = Director
    context_object_name = 'latest_director_list'
    template_name = 'movies/director_list.html'


class ActorList(ListView, ConnegResponseMixin):
    model = Actor
    context_object_name = 'latest_actor_list'
    template_name = 'movies/actor_list.html'


class CompanyList(ListView, ConnegResponseMixin):
    model = Company
    context_object_name = 'latest_company_list'
    template_name = 'movies/company_list.html'


class CountryList(ListView, ConnegResponseMixin):
    model = Country
    context_object_name = 'latest_country_list'
    template_name = 'movies/country_list.html'


class MovieDetail(DetailView, ConnegResponseMixin):
    model = Movie
    template_name = 'movies/movie_detail.html'

    def get_context_data(self, **kwargs):
        context = super(MovieDetail, self).get_context_data(**kwargs)
        return context


class DirectorDetail(DetailView, ConnegResponseMixin):
    model = Director
    template_name = 'movies/director_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DirectorDetail, self).get_context_data(**kwargs)
        context['movies'] = Movie.objects.filter(
            directors=Director.objects.filter(id=self.kwargs['pk']))
        return context


class ActorDetail(DetailView, ConnegResponseMixin):
    model = Actor
    template_name = 'movies/actor_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ActorDetail, self).get_context_data(**kwargs)
        context['movies'] = Movie.objects.filter(
            actors=Actor.objects.filter(id=self.kwargs['pk']))
        return context


class CompanyDetail(DetailView, ConnegResponseMixin):
    model = Company
    template_name = 'movies/company_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CompanyDetail, self).get_context_data(**kwargs)
        context['movies'] = Movie.objects.filter(
            companies=Company.objects.filter(id=self.kwargs['pk']))
        return context


class CountryDetail(DetailView, ConnegResponseMixin):
    model = Country
    template_name = 'movies/country_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CountryDetail, self).get_context_data(**kwargs)
        context['movies'] = Movie.objects.filter(
            countries=Country.objects.filter(id=self.kwargs['pk']))
        context['actors'] = Actor.objects.filter(
            country=Country.objects.filter(id=self.kwargs['pk']))
        context['directors'] = Director.objects.filter(
            country=Country.objects.filter(id=self.kwargs['pk']))
        context['companies'] = Company.objects.filter(
            country=Country.objects.filter(id=self.kwargs['pk']))
        return context


class MovieCreate(CreateView):
    model = Movie
    template_name = 'movies/form.html'
    form_class = MovieForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        form.instance.user = self.request.user
        self.object.save()
        return super(MovieCreate, self).form_valid(form)


class DirectorCreate(CreateView):
    model = Director
    template_name = 'movies/form.html'
    form_class = DirectorForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        form.instance.user = self.request.user
        self.object.save()
        return super(DirectorCreate, self).form_valid(form)


class ActorCreate(CreateView):
    model = Actor
    template_name = 'movies/form.html'
    form_class = ActorForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        form.instance.user = self.request.user
        self.object.save()
        return super(ActorCreate, self).form_valid(form)


class CompanyCreate(CreateView):
    model = Company
    template_name = 'movies/form.html'
    form_class = CompanyForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        form.instance.user = self.request.user
        self.object.save()
        return super(CompanyCreate, self).form_valid(form)


class CountryCreate(CreateView):
    model = Country
    template_name = 'movies/form.html'
    form_class = CountryForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        form.instance.user = self.request.user
        self.object.save()
        return super(CountryCreate, self).form_valid(form)

