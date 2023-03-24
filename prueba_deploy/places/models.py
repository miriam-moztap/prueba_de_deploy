from django.db import models

# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    description = models.CharField(max_length=256)

    class Meta:
        db_table = 'places'

    def __str__(self):
        return self.name
    

    