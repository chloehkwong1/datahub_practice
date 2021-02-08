from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers
from datahub.models import BedTemplate


from django_countries.serializer_fields import CountryField


class BedSerializer(CountryFieldMixin, serializers.ModelSerializer):

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
