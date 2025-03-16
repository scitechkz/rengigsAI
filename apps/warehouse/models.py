from django.db import models

# Create your models here.
class Rack(models.Model):
    location = models.CharField(max_length=100)
    capacity = models.IntegerField()
    occupied = models.BooleanField(default=False)

    def __str__(self):
        return self.location
