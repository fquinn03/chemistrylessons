# Create your views here.
from django.shortcuts import render


from resources.models import Resource

def home(request):
    return render(request, 'home.html', {})

def all_resources(request):
    all_resources = Resource.objects.filter(type="SAQ")
    context = {'all_resources': all_resources}

    return render(request, 'all_resources.html', context)
