# from django_countries.serializers import CountryFieldMixin
# from django_countries.serializer_fields import CountryField
from rest_framework import serializers
from datahub.models import BedTemplate


class BedSerializer(serializers.ModelSerializer):

    class Meta:
        model = BedTemplate
        fields = '__all__'
