from django.db import models

# Create your models here.


class Segment(models.Model):
    segment_name = models.CharField(max_length=100)

    def __str__(self):
        return self.segment_name
