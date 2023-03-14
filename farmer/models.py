import datetime
from django.db import models
import pytz 
from django.urls import reverse


from acc.models import User

# Create your models here.

class CropSeasonModel(models.Model):
    name            = models.CharField(max_length=1200)
    timestamp       = models.DateField(auto_now=False, auto_now_add=True)
    updated         = models.DateField(auto_now=True, auto_now_add=False)
    
    
    def __str__(self):
        return f'{self.name}'

    def __unicode__(self):
        return f'{self.name}'

class CropModel(models.Model):
    A = 'A'
    I = 'I'
    P = 'P'
    Medium = [ (A,'Active'), (P,'Pending'), (I,'Inactive'),]
    thumb           = models.ImageField(upload_to='crops/')
    name            = models.CharField(max_length=1200)
    type            = models.CharField(max_length=1200)
    season          = models.ForeignKey(CropSeasonModel, on_delete=models.CASCADE)
    description     = models.TextField()
    ogc             = models.TextField(verbose_name='optimum_growing_condition')
    market_value    = models.IntegerField()
    status          = models.CharField(max_length = 1, choices = Medium )
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
    farmer          = models.ManyToManyField(User)
    crop            = models.ManyToManyField(CropModel)
    timestamp       = models.DateField(auto_now=False, auto_now_add=True)
    updated         = models.DateField(auto_now=True, auto_now_add=False)

    def get_p(self):
        p = self.end - self.start
        return str(p)[:3]
    
    
    def get_days(self):
        days = self.get_today() - self.start
        return str(days)[:3] 
 
    def get_today(self):
        tz_utc = pytz.timezone('UTC')
        today = datetime.datetime.now() 
        dt_today_utc = tz_utc.localize(today)
        return dt_today_utc
 
    def get_period(self):
        return self.end - self.start
    
    def get_days_covered(self):
        return self.get_today() - self.start
            
        
    def get_progress(self):
        perc = (self.get_days_covered()/self.get_period()) * 100
        return round(perc,2)
    
    def get_is_complited(self):
        if int(self.get_progress()) < 99:
            return False
        else:
            return True
    
    def __str__(self):
        return f'{self.name}'

    def __unicode__(self):
        return f'{self.name}'

class ReportModel(models.Model):
    title           = models.CharField(max_length=50)
    discription     = models.TextField()
    item            = models.ForeignKey(CropRotationModel, on_delete=models.CASCADE,default=None) 
    timestamp       = models.DateField(auto_now=False, auto_now_add=True)
    updated         = models.DateField(auto_now=True, auto_now_add=False)
 
    class Meta:
        ordering = ['updated']
        
    def get_absolute_url(self):
        return reverse("farmer:add_report", kwargs={"pk": self.pk})
     
    def __str__(self):
        return f'{self.title}'

    def __unicode__(self):
        return f'{self.title}'
