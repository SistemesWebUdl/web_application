from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from django.core import serializers
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from rest_framework import generics, permissions
from django.contrib.auth.forms import UserCreationForm
from django.utils.decorators import method_decorator
from models import Movie, Director, Actor, Company, City
from forms import MovieForm, DirectorForm, ActorForm, CompanyForm, CityForm
from movies.serializers import MovieSerializer, ActorSerializer, CitySerializer, \
    CompanySerializer, DirectorSerializer




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


class LoginRequiredMixin(object):
    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj

class LoginRequiredCheckIsOwnerUpdateView(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    template_name = 'myrestaurants/form.html'

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


class CityList(ListView, ConnegResponseMixin):
    model = City
    context_object_name = 'latest_city_list'
    template_name = 'movies/city_list.html'


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


class CityDetail(DetailView, ConnegResponseMixin):
    model = City
    template_name = 'movies/city_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CityDetail, self).get_context_data(**kwargs)
        context['movies'] = Movie.objects.filter(
            cities=City.objects.filter(id=self.kwargs['pk']))
        context['actors'] = Actor.objects.filter(
            city=City.objects.filter(id=self.kwargs['pk']))
        context['directors'] = Director.objects.filter(
            city=City.objects.filter(id=self.kwargs['pk']))
        context['companies'] = Company.objects.filter(
            city=City.objects.filter(id=self.kwargs['pk']))
        return context


class MovieCreate(LoginRequiredMixin, CreateView):
    model = Movie
    template_name = 'movies/form.html'
    form_class = MovieForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        form.instance.user = self.request.user
        self.object.save()
        return super(MovieCreate, self).form_valid(form)


class MovieDelete(LoginRequiredCheckIsOwnerUpdateView, DeleteView):
    model = Movie
    template_name = 'movies/movie_confirm_delete.html'

    def get_success_url(self):
        return reverse('movies:movie_list', kwargs={'extension': 'html'})


class DirectorCreate(LoginRequiredMixin, CreateView):
    model = Director
    template_name = 'movies/form.html'
    form_class = DirectorForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        form.instance.user = self.request.user
        self.object.save()
        return super(DirectorCreate, self).form_valid(form)


class DirectorDelete(LoginRequiredCheckIsOwnerUpdateView, DeleteView):
    model = Director
    template_name = 'movies/director_confirm_delete.html'

    def get_success_url(self):
        return reverse('movies:director_list', kwargs={'extension': 'html'})


class ActorCreate(LoginRequiredMixin, CreateView):
    model = Actor
    template_name = 'movies/form.html'
    form_class = ActorForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        form.instance.user = self.request.user
        self.object.save()
        return super(ActorCreate, self).form_valid(form)


class ActorDelete(LoginRequiredCheckIsOwnerUpdateView, DeleteView):
    model = Actor
    template_name = 'movies/actor_confirm_delete.html'

    def get_success_url(self):
        return reverse('movies:actor_list', kwargs={'extension': 'html'})


class CompanyCreate(LoginRequiredMixin, CreateView):
    model = Company
    template_name = 'movies/form.html'
    form_class = CompanyForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        form.instance.user = self.request.user
        self.object.save()
        return super(CompanyCreate, self).form_valid(form)

class CompanyDelete(LoginRequiredCheckIsOwnerUpdateView, DeleteView):
    model = Company
    template_name = 'movies/company_confirm_delete.html'

    def get_success_url(self):
        return reverse('movies:company_list', kwargs={'extension': 'html'})


class CityCreate(LoginRequiredMixin, CreateView):
    model = City
    template_name = 'movies/form.html'
    form_class = CityForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        form.instance.user = self.request.user
        self.object.save()
        return super(CityCreate, self).form_valid(form)


class CityDelete(LoginRequiredCheckIsOwnerUpdateView, DeleteView):
    model = City
    template_name = 'movies/city_confirm_delete.html'

    def get_success_url(self):
        return reverse('movies:city_list', kwargs={'extension': 'html'})



class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Instance must have an attribute named `owner`.
        return obj.user == request.user


class APIMovieList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Movie.objects.all()
    model = Movie
    serializer_class = MovieSerializer


class APIMovieDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Movie.objects.all()
    model = Movie
    serializer_class = MovieSerializer


class APIActorList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Actor.objects.all()
    model = Actor
    serializer_class = ActorSerializer


class APIActorDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Actor.objects.all()
    model = Actor
    serializer_class = ActorSerializer


class APIDirectorList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Director.objects.all()
    model = Director
    serializer_class = DirectorSerializer


class APIDirectorDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Director.objects.all()
    model = Director
    serializer_class = DirectorSerializer


class APICompanyList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Company.objects.all()
    model = Company
    serializer_class = CompanySerializer


class APICompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Company.objects.all()
    model = Company
    serializer_class = CompanySerializer


class APICityList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = City.objects.all()
    model = City
    serializer_class = CitySerializer


class APICityDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = City.objects.all()
    model = City
    serializer_class = CitySerializer




class UserCreate(CreateView):
    model = User
    template_name = 'movies/form.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('movies:movie_list', kwargs={'extension': 'html', })

    def form_valid(self, form):
        self.object = form.save(commit=False)
        form.instance.user = self.request.user
        self.object.save()
        return super(UserCreate, self).form_valid(form)
