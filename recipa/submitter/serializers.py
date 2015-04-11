from rest_framework import serializers
from submitter.models import *


class CitySerializer(serializers.ModelSerializer):
    state = serializers.StringRelatedField()

    class Meta:
        model = City
        fields = ('cityname', 'state')


class SubmitterSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = Submitter
        fields = ('submitterid', 'firstname', 'lastname', 'city')