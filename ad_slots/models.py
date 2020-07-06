from django.db import models

# Create your models here.


class Ad_Slot(models.Model):
    slot_id = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.slot_id
