from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple
from models import Movie, Director, Actor, Company, Country

class MovieForm(ModelForm):
    actors = ModelMultipleChoiceField(widget=CheckboxSelectMultiple,
                                      queryset=Actor.objects.all())
    directors = ModelMultipleChoiceField(widget=CheckboxSelectMultiple,
                                         queryset=Director.objects.all())
    companies = ModelMultipleChoiceField(widget=CheckboxSelectMultiple,
                                         queryset=Company.objects.all())
    countries = ModelMultipleChoiceField(widget=CheckboxSelectMultiple,
                                         queryset=Country.objects.all())

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

class CountryForm(ModelForm):
    class Meta:
        model = Country
        exclude = ('user', 'date',)

class ActorAddForm(ModelForm):
    actors = ModelMultipleChoiceField(widget=CheckboxSelectMultiple,
                                      queryset=Actor.objects.all())

    class Meta:
        model = Movie
        fields = ('actors',)

class DirectorAddForm(ModelForm):
    directors = ModelMultipleChoiceField(widget=CheckboxSelectMultiple,
                                        queryset=Director.objects.all())

    class Meta:
        model = Movie
        fields = ('directors',)

class CompanyAddForm(ModelForm):
    companies = ModelMultipleChoiceField(widget=CheckboxSelectMultiple,
                                         queryset=Company.objects.all())

    class Meta:
        model = Movie
        fields = ('companies',)

class CountryAddForm(ModelForm):
    countries = ModelMultipleChoiceField(widget=CheckboxSelectMultiple,
                                         queryset=Country.objects.all())

    class Meta:
        model = Movie
        fields = ('countries',)


class CountryDirectorForm(ModelForm):

    class Meta:
        model = Director
        fields = ('country',)

class CountryActorForm(ModelForm):

    class Meta:
        model = Actor
        fields = ('country',)

class CountryCompanyForm(ModelForm):

    class Meta:
        model = Company
        fields = ('country',)
