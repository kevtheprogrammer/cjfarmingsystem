from django.contrib import admin
from .models import * 

admin.site.register([CropSeasonModel,CropModel,FarmPlotModel,CropRotationModel])
