from django.db import models

# Create your models here.
from django.db import models


class Deposit(models.Model):
    description = models.CharField(max_length=125)
    Interest = models.InterestField()
    Rate = models.RateField()
    Term = models.TermField()
    def __str__(self):
        return f'{self.pk} [{self.description}]'


class Deposit(models.Model):

    deposit = models.CharField(max_length=125)
    Interest = models.InterestField()
    Rate = models.RateField()
    Term = models.TermField()