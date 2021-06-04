from django.db import models
from django.contrib.auth.models import User


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key=True)
    TEACHER = 'T'
    STUDENT = 'S'
    PARENT = 'P'
    USER_CHOICES = [
        (TEACHER, 'Teacher'),
        (STUDENT, 'Student'),
        (PARENT, 'Parent'),
    ]
    status = models.CharField(
        max_length=1,
        choices=USER_CHOICES,
        default=TEACHER,
    )
    subscribed = models.BooleanField(default=False)


