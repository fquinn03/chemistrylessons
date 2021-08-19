# Create your views here.
from django.shortcuts import render


from resources.models import Resource

def home(request):
    return render(request, 'home.html', {})

def all_resources(request):
    topic = request.POST.get('topic')
    resources = Resource.objects.all()
    resources = resources.filter(topic = topic)

    return render(request, 'all_resources.html', {'resources': resources })
