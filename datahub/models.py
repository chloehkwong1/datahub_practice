from django.db import models
import uuid


class BEDTemplate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    interaction_title = models.CharField(max_length=200, unique=True)
    interaction_date = models.DateField()
    lead_minister_or_official = models.EmailField()
    type = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    city_or_town = models.CharField(max_length=200)
    attending_organisations = models.TextField()
    attending_contacts = models.TextField()

    def __str__(self):
        return f"{self.interaction_date} {self.interaction_title}"

class Csv(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file_name = models.FileField(upload_to='csvs')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"File id: {self.id}"