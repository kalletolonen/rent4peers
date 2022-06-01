from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User

class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    description = models.TextField(default="Enter a short description here.")
    owner = models.ForeignKey(
            User,
            on_delete=models.CASCADE, default=""
        )

    def __str__(self):
        return f"{self.pk}. {self.name}"

    def get_absolute_url(self):
        return f"/vehicle/{self.pk}" 

class RentInstance(models.Model):
    def get_duedate():
        return datetime.today() + timedelta(days=7)

    def get_total_rent(self):
        return self.dayprice * (self.end - self.start).days
        
    def __str__(self):
        return f"{self.pk}. {self.vehicle} PERIOD: {self.start} - {self.end}"

    def get_absolute_url(self):
        return f"/rent/{self.pk}" 

    #Ask about changing function names and migrations!
    #How to make the default daily rate so that you can do revenue management?
    #How to make a default rent period from monday to sunday?
    
    vehicle = models.ForeignKey('Vehicle', null=True,on_delete=models.SET_NULL)
    start = models.DateField(null=True, blank=True, default=datetime.today)
    end = models.DateField(null=True, blank=True, default=get_duedate)
    dayprice = models.DecimalField(default=100.0, max_digits=20, decimal_places=2)
    renter = models.ForeignKey(
            User,
            on_delete=models.CASCADE, default=""
        )
        
    RENT_STATUS = (
            ('C', 'Confirmed'),
            ('A', 'Available'),
            ('R', 'Reserved'),
            ('M', 'Maintenance'),
            ('P', 'Personal use'),
        )
    status = models.CharField(
            max_length=1,
            choices=RENT_STATUS,
            blank=True,
            default='a',
            help_text='Vehicle availability',
        )     

    

