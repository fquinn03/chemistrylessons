from django.db import models
from django.contrib.auth.models import User


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key=True)
    user_type = models.CharField(max_length=200);


