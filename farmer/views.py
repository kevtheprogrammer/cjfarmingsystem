from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import Group
from django.views.generic.edit import CreateView, DeleteView, UpdateView 
from django.views.generic import ListView , DetailView ,View,TemplateView
from . models import *
from acc.userForms import *
from acc.models import *


class AdminView(TemplateView):
    template_name = "admin/mngmnt/index.html"

    def get(self, request,**kwargs):
        me = self.request.user
        group = None
        if me.groups.exists():
            group = me.groups.all()[0].name
        if group == 'Farmers':
            context = super().get_context_data(**kwargs)
            cnt = {   
                "cm"    :  CropModel.objects.all(),
                "csm"   :  CropSeasonModel.objects.all(),
                "users" :  User.objects.all(),
                "crm"   :  CropRotationModel.objects.filter(farmer=me),
            }
            return render(request,self.template_name, cnt)
        return redirect('farmer:registration')
            
class RegistraionView(CreateView):
    model = User
    form_class = UserEditForm
    template_name = "admin/mngmnt/registration.html"
    
    def get(self, request, *args, **kwargs):
        me = self.request.user
        context = {
            "form":self.form_class(instance=me),
        } 
        return render(request,self.template_name,context)

    def post(self, request, *args, **kwargs): 
        me = self.request.user
        forms = self.form_class(self.request.POST,self.request.FILES,instance=me)
        group = None
        if forms.is_valid():
            forms.save()
            if me.groups.exists():
                group = me.groups.all()[0].name
            if group != 'Farmers':
                my_group = Group.objects.get(name='Farmers') 
                my_group.user_set.add(me)
                me.email_farmer_registration(
                    subject = "Request to Register as a Farmer", 
                    message = "Request to Register as a Farmer was success do login at http://localhost:8000/administration/ to access our services", 
                    from_email="cityofjehovarfarmingsystem@support.com"
                )
            return redirect("farmer:index")
        return render(request,self.template_name)



class FarmerDetiails(CreateView):
    template_name = 'admin/mngmnt/farmer_index.html'
    models = User
    form_class = UserEditForm

    def get(self, request, *args, **kwargs):
        me = self.request.user
        
        myplot = FarmPlotModel.objects.get(user__id=me.id)
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
