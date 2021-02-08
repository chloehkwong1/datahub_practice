from django.db import models
from django_countries.fields import CountryField
import uuid


class BedTemplate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    interaction_title = models.CharField(max_length=200, unique=True,
                                         help_text='This is the title of the interaction, for example "XYZ meeting"')
    interaction_date = models.DateField(help_text='The date of the interaction, in a yyyy-mm-dd format.')
    lead_minister_or_official = models.EmailField(
        help_text='The e-mail address of the minister or official who led the engagement.')
    type = models.CharField(
        choices=[('bilateral_meeting', 'Bilateral Meeting'),
                 ('brush_by', 'Brush By'),
                 ('conference', 'Conference'),
                 ('email', 'Email'),
                 ('forum', 'Forum'),
                 ('letter', 'Letter'),
                 ('multilateral_meeting', 'Multilateral Meeting'),
                 ('phone_call', 'Phone Call'),
                 ('reception', 'Reception'),
                 ('roadshow', 'Roadshow'),
                 ('roundtable', 'Roundtable'),
                 ('speech', 'Speech'),
                 ('visit', 'Visit'),
                 ('webinar', 'Webinar')
                 ],
        max_length=200,
        help_text='See guidance for examples of types.'
    )
    country = CountryField(max_length=200, help_text='Please select from the list below.')
    ## country field needs changing as json serialiser doesn't work with uploaded csvs
    region = models.CharField(
        choices=[('london', 'London'),
                 ('scotland', 'Scotland'),
                 ('wales', 'Wales'),
                 ('northern_ireland', 'Northern Ireland'),
                 ('east_of_england', 'East of England'),
                 ('east_midlands', 'East Midlands'),
                 ('north_east', 'North East'),
                 ('south_east', 'South East'),
                 ('south_west', 'South West'),
                 ('west_midlands', 'West Midlands'),
                 ('yorkshire_and_the_humber', 'Yorkshire and the Humber'),
                 ('guernsey', 'Guernsey'),
                 ('jersey', 'Jersey'),
                 ('isle_of_man', 'Isle of Man'),
                 ('non_uk', 'Non UK')
                 ],
        max_length=200, help_text='Please select from the list below.')
    city_or_town = models.CharField(max_length=200, help_text='For example Bristol, Brighton or Chelmsford.')
    attending_organisations = models.TextField(help_text='A list of organisations who attended, separated by a comma.')
    attending_contacts = models.TextField(
        help_text='A list of attendees (by e-mail address) who attended, separated by a comma.')

    def __str__(self):
        return f"{self.interaction_date} {self.interaction_title}"


class Csv(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file_name = models.FileField(upload_to='csvs')
    uploaded = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return f"File name: {self.file_name}"
