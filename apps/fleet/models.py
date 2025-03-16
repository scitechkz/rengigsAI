from django.db import models

# Create your models here.
class Driver(models.Model):
    name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50, unique=True)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name
