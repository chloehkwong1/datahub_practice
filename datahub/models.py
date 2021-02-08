from django.db import models
from django_countries.fields import CountryField
import uuid


class BedTemplate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    interaction_title = models.CharField(max_length=200, unique=True)
    interaction_date = models.DateField()
    lead_minister_or_official = models.EmailField()
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
        max_length=100
    )
    country = CountryField(blank_label='(select country)', max_length=100)
    region = models.CharField(max_length=100)
    city_or_town = models.CharField(max_length=100)
    attending_organisations = models.TextField()
    attending_contacts = models.TextField()

    def __str__(self):
        return f"{self.interaction_date} {self.interaction_title}"


class Csv(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file_name = models.FileField(upload_to='csvs')
    uploaded = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return f"File name: {self.file_name}"
