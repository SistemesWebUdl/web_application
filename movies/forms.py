from django.core.exceptions import NON_FIELD_ERRORS
from django.forms import ModelForm, ModelMultipleChoiceField, forms
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

class ActorAddForm(ModelForm):

    class Meta:
        model = Movie
        fields = ('actors',)

class DirectorAddForm(ModelForm):

    class Meta:
        model = Movie
        fields = ('directors',)

class CompanyAddForm(ModelForm):

    class Meta:
        model = Movie
        fields = ('companies',)
