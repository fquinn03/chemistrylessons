from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all_resources', views.all_resources, name='all_resources'),

]