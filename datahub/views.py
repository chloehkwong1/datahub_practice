from django.http import HttpResponse
from django.shortcuts import render
from .forms import CsvModelForm
from .models import Csv, BEDTemplate
from dateutil.parser import parse

import csv


def index(request):
    return HttpResponse('Welcome to DIT Datahub.')


def upload_file_view(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else:
                    BEDTemplate.objects.create(
                        interaction_title=row[0],
                        interaction_date=parse(row[1]),
                        lead_minister_or_official=row[2],
                        type=row[3],
                        country=row[4],
                        region=row[5],
                        city_or_town=row[6],
                        attending_organisations=row[7],
                        attending_contacts=row[8],
                    )
                obj.activated = True
                obj.save()
    return render(request, 'upload.html', {'form': form})
