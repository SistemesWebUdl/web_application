from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple
from models import Movie, Director, Actor, Company, City


class MovieForm(ModelForm):
    actors = ModelMultipleChoiceField(widget=CheckboxSelectMultiple,
                                      queryset=Actor.objects.all(),
                                      required=False)
    directors = ModelMultipleChoiceField(widget=CheckboxSelectMultiple,
                                         queryset=Director.objects.all(),
                                         required=False)
    companies = ModelMultipleChoiceField(widget=CheckboxSelectMultiple,
                                         queryset=Company.objects.all(),
                                         required=False)
    cities = ModelMultipleChoiceField(widget=CheckboxSelectMultiple,
                                      queryset=City.objects.all(),
                                      required=False)

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


class CityForm(ModelForm):
    class Meta:
        model = City
        exclude = ('user', 'date',)


class ActorAddForm(ModelForm):
    actors = ModelMultipleChoiceField(widget=CheckboxSelectMultiple,
                                      queryset=Actor.objects.all(),
                                      required=False)

    class Meta:
        model = Movie
        fields = ('actors',)


class DirectorAddForm(ModelForm):
    directors = ModelMultipleChoiceField(widget=CheckboxSelectMultiple,
                                         queryset=Director.objects.all(),
                                         required=False)

    class Meta:
        model = Movie
        fields = ('directors',)


class CompanyAddForm(ModelForm):
    companies = ModelMultipleChoiceField(widget=CheckboxSelectMultiple,
                                         queryset=Company.objects.all(),
                                         required=False)

    class Meta:
        model = Movie
        fields = ('companies',)


class CityAddForm(ModelForm):
    countries = ModelMultipleChoiceField(widget=CheckboxSelectMultiple,
                                         queryset=City.objects.all(),
                                         required=False)

    class Meta:
        model = Movie
        fields = ('cities',)


class CityDirectorForm(ModelForm):

    class Meta:
        model = Director
        fields = ('city',)


class CityActorForm(ModelForm):

    class Meta:
        model = Actor
        fields = ('city',)


class CityCompanyForm(ModelForm):

    class Meta:
        model = Company
        fields = ('city',)
