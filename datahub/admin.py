from django.contrib import admin

# Register your models here.
from .models import BedTemplate, Csv

admin.site.register(BedTemplate)
admin.site.register(Csv)