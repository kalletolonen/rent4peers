from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

class VehicleListView(ListView): 
    model = models.Vehicle
    
class VehicleDetailView(DetailView): 
    model = models.Vehicle
    fields = ['name','manufacturer','description']
    
class VehicleUpdateView(LoginRequiredMixin, UpdateView): 
    def get_queryset(self):
    	return models.Vehicle.objects.filter(owner=self.request.user)

    fields = ['name','manufacturer','description']

class VehicleCreateView(LoginRequiredMixin, CreateView): 
    model = models.Vehicle
    fields = ['name','manufacturer','description']
    success_url = "/vehicle"

    def form_valid(self, form):
    	form.instance.owner = self.request.user #who made the form request
    	return super().form_valid(form) #call CreateView

class VehicleDeleteView(LoginRequiredMixin, DeleteView): 
    def get_queryset(self):
    	return models.Vehicle.objects.filter(owner=self.request.user)

#RENT INSTANCES
class RentListView(ListView):
    model = models.RentInstance

class RentCreateView(LoginRequiredMixin, CreateView): 
    model = models.RentInstance
    fields = ['vehicle','start','end']
    success_url = "/rent"

    #Function to customize fields for renters and owners
    #Has to be on status Available to be able to rent for the period   	    

    def form_valid(self, form):
    	form.instance.renter = self.request.user
    	return super().form_valid(form)

class RentUpdateView(LoginRequiredMixin, UpdateView): 

    #How to get only the cars the user owns
    def get_queryset(self):
        return models.RentInstance.objects.filter(vehicle__owner=self.request.user)
    
    fields = ['start','end','dayprice','status']
    success_url = "/rent"

class RentDeleteView(LoginRequiredMixin, DeleteView): 
    def get_queryset(self):
        return models.RentInstance.objects.filter(vehicle__owner=self.request.user)

#REGISTER
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = "/accounts/login"
