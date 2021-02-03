from django.contrib import admin

# Register your models here.
from .models import BEDTemplate, Csv

admin.site.register(BEDTemplate)
admin.site.register(Csv)