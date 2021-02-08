from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from .forms import CsvModelForm
from .models import Csv, BedTemplate
from .serializers import BedSerializer
from rest_framework.decorators import api_view
from dateutil.parser import parse

import csv

def upload_file_view(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(published=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else:
                    BedTemplate.objects.create(
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
                obj.published = True
                obj.save()
    return render(request, 'upload.html', {'form': form})

@api_view(['GET', 'POST'])
def interaction_list(request):
    # GET list of interactions, POST a new interaction
    if request.method == 'GET':
        interactions = BedTemplate.objects.all()

        title = request.GET.get('interaction_title', None)
        if title is not None:
            interactions = interactions.filter(interaction_title__icontains=title)

        interactions_serializer = BedSerializer(interactions, many=True)
        return JsonResponse(interactions_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        interaction_data = JSONParser().parse(request)
        interaction_serializer = BedSerializer(data=interaction_data)
        if interaction_serializer.is_valid():
            interaction_serializer.save()
            return JsonResponse(interaction_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(interaction_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def interaction_detail(request, pk):
    # find interaction by id
    try:
        interaction = BedTemplate.objects.get(pk=pk)
    except BedTemplate.DoesNotExist:
        return JsonResponse({'message': 'This interaction does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        interaction_serializer = BedSerializer(interaction)
        return JsonResponse(interaction_serializer.data)

    elif request.method == 'PUT':
        interaction_data = JSONParser().parse(request)
        interaction_serializer = BedSerializer(interaction, data=interaction_data)
        if interaction_serializer.is_valid():
            interaction_serializer.save()
            return JsonResponse(interaction_serializer.data)
        return JsonResponse(interaction_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        interaction.delete()
        return JsonResponse({'message': 'Interaction was deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)




@api_view(['GET'])
def interaction_list_published(request):
    # GET all published interactions
    interactions = BedTemplate.objects.filter(published=True)

    if request.method == 'GET':
        interactions_serializer = BedSerializer(interactions, many=True)
        return JsonResponse(interactions_serializer, safe=False)