from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key=True)
    TEACHER = 'T'
    STUDENT = 'S'
    PARENT = 'P'
    UNSUBSCRIBED = 'US'
    USER_CHOICES = [
        (TEACHER, 'Teacher'),
        (STUDENT, 'Student'),
        (PARENT, 'Parent'),
        (UNSUBSCRIBED, 'Unsubscribed'),
    ]
    status = models.CharField(
        max_length=2,
        choices=USER_CHOICES,
        default= UNSUBSCRIBED,
    )
    subscribed = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        CustomUser.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.customuser.save()