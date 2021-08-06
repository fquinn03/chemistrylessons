from django.db import models

# Create your models here.

class Resource(models.Model):
    SHORTANSWERQUIZ = 'SAQ'
    KEYWORDMATCHING = 'KWM'
    NOTES = 'N'
    PRACTICEDRILLS = 'PD'
    VIDEO = 'video'
    PDF = 'PDF'
    WORD = 'Word'

    TYPES = [
        (SHORTANSWERQUIZ, 'Short Answer Quiz'),
        (KEYWORDMATCHING, 'Keyword Matching'),
        (NOTES , 'Notes'),
        (PRACTICEDRILLS, 'Practice Drills'),
    ]

    FORMATS = [
        (VIDEO, 'Video'),
        (PDF, 'PDF'),
        (WORD, 'Word'),
    ]

    title = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    free = models.BooleanField(default=False)
    description = models.CharField(max_length=300)
    type = models.CharField(max_length=3, choices=TYPES)
    format = models.CharField(max_length=20, choices=FORMATS)
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.topic+": "+self.title