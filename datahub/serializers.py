# from django_countries.serializers import CountryFieldMixin
# from django_countries.serializer_fields import CountryField
from rest_framework import serializers
from datahub.models import BedTemplate


class BedSerializer(serializers.ModelSerializer):

    class Meta:
        model = BedTemplate
        fields = (
            'id',
            'interaction_title',
            'interaction_date',
            'lead_minister_or_official',
            'type',
            'country',
            'region',
            'city_or_town',
            'attending_organisations',
            'attending_contacts',
        )
