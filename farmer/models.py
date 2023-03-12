import datetime
from django.db import models

from acc.models import User

# Create your models here.

class CropSeasonModel(models.Model):
    name   = models.CharField(max_length=1200)
    timestamp       = models.DateField(auto_now=False, auto_now_add=True)
    updated         = models.DateField(auto_now=True, auto_now_add=False)
    
    
    def __str__(self):
        return f'{self.name}'

    def __unicode__(self):
        return f'{self.name}'


class CropModel(models.Model):
    
    A = 'A'
    N = 'N'
    P = 'P'
    
    Medium = [
        (A,'Active'),
        (N,'Active'),
        (P,'Pending'),
    ]
    thumb   = models.ImageField(upload_to='crops/')
    name   = models.CharField(max_length=1200)
    type   = models.CharField(max_length=1200)
    season = models.ForeignKey(CropSeasonModel, on_delete=models.CASCADE)
    description = models.TextField()
    ogc = models.TextField(verbose_name='optimum_growing_condition')
    market_value = models.IntegerField()
    status      = models.CharField(max_length = 1, choices = Medium )
    timestamp       = models.DateField(auto_now=False, auto_now_add=True)
    updated         = models.DateField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return f'{self.name}'

    def __unicode__(self):
        return f'{self.name}'
 
class FarmPlotModel(models.Model):
    name   = models.CharField(max_length=1200)
    size   = models.CharField(max_length=1200)
    farm_location  = models.CharField(max_length=1200)
    Soil_type = models.CharField(max_length=1200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    def __unicode__(self):
        return f'{self.name}'

class CropRotationModel(models.Model):
    start           = models.DateTimeField( default=None,auto_now=False, auto_now_add=False)
    end             = models.DateTimeField( default=None,auto_now=False, auto_now_add=False)
    name            = models.CharField(max_length=1200)
    farmer          = models.ForeignKey(User, on_delete=models.CASCADE)
    crop            = models.ForeignKey(CropModel, on_delete=models.CASCADE)
    timestamp       = models.DateField(auto_now=False, auto_now_add=True)
    updated         = models.DateField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return f'{self.name}'

    def __unicode__(self):
        return f'{self.name}'



# class ReportModel(models.Model):
#     title = models.CharField(max_length=50)
#     discription = models.TextField()
#     item = models.ForeignKey(CropRotationModel, on_delete=models.CASCADE,default=None) 
#     timestamp       = models.DateField(auto_now=False, auto_now_add=True)
#     updated         = models.DateField(auto_now=True, auto_now_add=False)
    
#     def __str__(self):
#         return f'{self.title}'

#     def __unicode__(self):
#         return f'{self.title}'
