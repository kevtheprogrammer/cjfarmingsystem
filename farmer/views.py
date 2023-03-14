from django.shortcuts import get_object_or_404, render,redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView 
from django.views.generic import ListView , DetailView ,View,TemplateView
from . models import *
from acc.userForms import *
from acc.models import *


class AdminView(TemplateView):
    template_name = "admin/mngmnt/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        me = self.request.user
        context["csm"] = CropSeasonModel.objects.all()
        context["cm"] = CropModel.objects.all()
        context["users"] = User.objects.all()
        context["crm"] = CropRotationModel.objects.filter(farmer=me)
        return context

class FarmerDetiails(CreateView):
    template_name = 'admin/mngmnt/farmer_index.html'
    models = User
    form_class = UserEditForm

    def get(self, request, *args, **kwargs):
        me = self.request.user
        
        myplot = FarmPlotModel.objects.get(user__id=me.id)
        print(myplot)
        context = {
            "form":self.form_class(instance=me),
            "User":User.objects.get(id=me.id),
            "plot":FarmPlotForm(instance=myplot)
        } 
        return render(request,self.template_name,context)


    def post(self, request, *args, **kwargs): 
        me = self.request.user
        forms = UserEditForm(self.request.POST,self.request.FILES,instance=me)
        plot_form = UserEditForm(self.request.POST)
        if forms.is_valid():
            forms.save()
            return redirect("farmer:f_details")
        if plot_form.is_valid():
            newf = plot_form.save(False)
            newf.user = me
            newf.save()
            return redirect("farmer:f_details")

        return render(request,self.template_name)


class ViewReport(TemplateView):
    template_name = 'admin/mngmnt/view_report.html'
    models = User
    form_class = FarmerReportForm
    
    def get(self,request, **kwargs):
        me = self.request.user
        context = {
            "report" : ReportModel.objects.filter(item__farmer=me),
            "form":FarmerReportForm(),
            
        }
        return render(request,self.template_name,context)
    
    def post(self, request, *args, **kwargs): 
        forms = FarmerReportForm(self.request.POST)
        if forms.is_valid():
            forms.save()
            return redirect("farmer:report")
        return render(request,self.template_name)
    
    
    
class MakeReport(DetailView):
    template_name = 'admin/mngmnt/make_report.html'
    model = ReportModel
    
    def get(self, request,pk, *args, **kwargs):
        myItem = get_object_or_404(ReportModel,pk=pk)
        context = { 
            "form":FarmerReportForm(instance=myItem),
            "object":myItem,
        } 
        return render(request,self.template_name,context)


    def post(self, request, pk, *args, **kwargs): 
        myItem = get_object_or_404(ReportModel,pk=pk)
        forms = FarmerReportForm(self.request.POST,instance=myItem)
        if forms.is_valid():
            forms.save()
            return redirect("farmer:report")
        return render(request,self.template_name)
