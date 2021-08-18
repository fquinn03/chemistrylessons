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
    TOPIC_1 = "KC"
    TOPIC_2 = "SLG&M"
    TOPIC_3 = "CC"
    TOPIC_4 = "EM&E"
    TOPIC_5 = "SC1"
    TOPIC_6 = "PT"
    TOPIC_7 = "ROR"
    TOPIC_8 = "F&ES"
    TOPIC_9 = "SC2"


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

    TOPICS = [
        (TOPIC_1,'Key concepts in chemistry'),
        (TOPIC_2,'States of matter and mixtures'),
        (TOPIC_3,'Chemical changes'),
        (TOPIC_4,'Extracting metals and equilibria'),
        (TOPIC_5,'Separate chemistry 1'),
        (TOPIC_6,'Groups in the periodic table'),
        (TOPIC_7,'Rates of reaction and energy changes'),
        (TOPIC_8,'Fuels and Earth science'),
        (TOPIC_9,'Separate chemistry 2'),
    ]

    title = models.CharField(max_length=50)
    topic = models.CharField(max_length=5, choices=TOPICS)
    description = models.CharField(max_length=200)
    free = models.BooleanField(default=False)
    type = models.CharField(max_length=3, choices=TYPES)
    format = models.CharField(max_length=10, choices=FORMATS)
    link = models.CharField(max_length=80)

    def __str__(self):
        return self.type+": "+ self.topic+", "+self.title