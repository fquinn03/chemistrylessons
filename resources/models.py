from django.db import models

# Create your models here.
class Lesson(models.Model):
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False, null=False)
    number = models.IntegerField()
    location = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'lesson'

class Topic(models.Model):

    title = models.CharField(max_length=100, blank=False, null=False)
    level = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'topic'

    def __str__(self):
        return self.title
