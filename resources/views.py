from django.shortcuts import render

# Create your views here.

def all_resources(request):
    return render(request, 'all_resources.html', {})