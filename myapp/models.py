from operator import mod
from django.db import models

# Create your models here.
class Creditcard(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Aadhar = models.IntegerField(unique=True)

    def __str__(self):
        return self.Name
  