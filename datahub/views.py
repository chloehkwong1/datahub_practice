from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to DIT Datahub.")

# Create your views here.
