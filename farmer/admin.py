from django.contrib import admin
from .models import * 

@admin.register(CropSeasonModel)
class CropSeasonModelAdmin(admin.ModelAdmin):
    list_display = ('name','timestamp', 'updated', )
    list_filter = ('updated',)
    search_fields = ('name',) 
 
@admin.register(CropModel)
class CropModelAdmin(admin.ModelAdmin):
    list_display = ('name','type', 'season', 'market_value','status',)
    list_filter = ('status', 'market_value',)
    search_fields = ('name',) 

@admin.register(FarmPlotModel)
class FarmPlotModelAdmin(admin.ModelAdmin):
    list_display = ('name','size', 'farm_location','Soil_type',)
    search_fields = ('name',) 
 
@admin.register(CropRotationModel)
class CropRotationModelAdmin(admin.ModelAdmin):
    list_display = ('name','start', 'end',)
    search_fields = ('name',) 

@admin.register(ReportModel)
class ReportModelAdmin(admin.ModelAdmin):
    list_display = ('title','discription', 'item','updated',)
    search_fields = ('title',) 


