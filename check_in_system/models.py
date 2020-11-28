from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Visitor(models.Model):
    owner =  models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 150)
    id_number = models.CharField(max_length=150, blank = True)
    telephone_number = models.IntegerField()
    temperature = models.DecimalField(max_digits = 3, decimal_places = 1)
    company = models.CharField(max_length = 150)
    date = models.DateField(default=timezone.now)

def __str__(self):
    return self.name