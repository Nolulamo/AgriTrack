from django.db import models
from django.contrib.auth.models import User

class Nutrient(models.Model):
    nitrogen = models.IntegerField()
    phosphorus = models.IntegerField()
    potassiun = models.IntegerField()
    pH = models.IntegerField()
    ec = models.IntegerField()
    moisture = models.IntegerField()
    temperature = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ('-date_created',)


class Settings(models.Model):
    MEDIUM_CHOICES = [
        ('H', 'Hydroponics'),
        ('CS', 'Clay Soil'),
        ('LS', 'Loam Soil'),
        ('SS', 'Sandy Soil'),
    ]

    STAGE_CHOICES = [
        ('VS', 'vegitation Stage'),
        ('FS', 'Fruiting Stage'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    medium = models.CharField(choices=MEDIUM_CHOICES, max_length=2, default='CS')
    stage = models.CharField(choices=STAGE_CHOICES, max_length=2, default='VS')

    def __str__(self):
        return self.user.first_name

