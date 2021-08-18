# Create your views here.
from django.shortcuts import render


from resources.models import Resource

def home(request):
    return render(request, 'home.html', {})

def all_resources(request):
    saqs = Resource.objects.filter(type="SAQ")
    notes = Resource.objects.filter(type="N")
    return render(request, 'all_resources.html', {'saqs': saqs, 'notes':notes})
