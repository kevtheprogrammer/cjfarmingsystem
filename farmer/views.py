from django.shortcuts import render

from django.views.generic.edit import CreateView, DeleteView, UpdateView 
from django.views.generic import ListView , DetailView ,View,TemplateView
from . models import *


class AdminView(TemplateView):
    template_name = "admin/mngmnt/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["csm"] = CropSeasonModel
        context["cm"] = CropModel
        context["fp"] = FarmPlotModel
        context["crm"] = CropRotationModel
        return context
    







