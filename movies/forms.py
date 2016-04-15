from django.forms import ModelForm
from models import Movie, Director, Actor, Company

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        exclude = ('user', 'date',)

class DirectorForm(ModelForm):
    class Meta:
        model = Director
        exclude = ('user', 'date',)

class ActorForm(ModelForm):
    class Meta:
        model = Actor
        exclude = ('user', 'date',)

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        exclude = ('user', 'date',)
