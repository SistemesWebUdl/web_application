from rest_framework import serializers, relations, fields
from movies.models import Movie, Actor, Director, Company, City


class MovieSerializer(serializers.HyperlinkedModelSerializer):

    uri = relations.HyperlinkedIdentityField(view_name='movies:movie-detail')
    actors = relations.HyperlinkedRelatedField(many=True, read_only=True,
                                               view_name='movies:actor-detail')
    cities = relations.HyperlinkedRelatedField(many=True, read_only=True,
                                               view_name='movies:city-detail')
    directors = relations.HyperlinkedRelatedField(many=True, read_only=True,
                                                  view_name='movies:director-detail')
    companies = relations.HyperlinkedRelatedField(many=True, read_only=True,
                                                  view_name='movies:company-detail')
    user = fields.CharField(read_only=True)

    class Meta:
        model = Movie
        fields = ('uri', 'movie_name', 'movie_release_date', 'description', 'image',
                  'actors', 'directors', 'companies', 'cities', 'user', 'date')


class ActorSerializer(serializers.HyperlinkedModelSerializer):

    uri = relations.HyperlinkedIdentityField(view_name='movies:actor-detail')
    city = relations.HyperlinkedRelatedField(read_only=True,
                                             view_name='movies:city-detail')
    user = fields.CharField(read_only=True)

    class Meta:
        model = Actor
        fields = ('uri', 'name', 'birthday', 'deathday', 'city', 'url',
                  'image', 'user', 'date')


class DirectorSerializer(serializers.HyperlinkedModelSerializer):

    uri = relations.HyperlinkedIdentityField(view_name='movies:director-detail')
    city = relations.HyperlinkedRelatedField(read_only=True,
                                             view_name='movies:city-detail')
    user = fields.CharField(read_only=True)

    class Meta:
        model = Actor
        fields = ('uri', 'name', 'birthday', 'deathday', 'city', 'url',
                  'image', 'user', 'date')


class CompanySerializer(serializers.HyperlinkedModelSerializer):

    uri = relations.HyperlinkedIdentityField(view_name='movies:company-detail')
    city = relations.HyperlinkedRelatedField(read_only=True,
                                             view_name='movies:city-detail')
    user = fields.CharField(read_only=True)

    class Meta:
        model = Company
        fields = ('uri', 'company_name', 'description', 'url', 'city', 'user', 'date')


class CitySerializer(serializers.HyperlinkedModelSerializer):

    uri = relations.HyperlinkedIdentityField(view_name='movies:city-detail')
    user = fields.CharField(read_only=True)

    class Meta:
        model = City
        fields = ('uri', 'city_name', 'stateOrProvince', 'country', 'user', 'date')
