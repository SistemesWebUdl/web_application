from django.forms import ModelForm
from models import Movie, Director, Actor

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
