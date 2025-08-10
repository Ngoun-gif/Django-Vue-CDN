from django.contrib import admin 
from backend.models import Customer, Service, Category , Branch  , Booking
# Register your models here.
admin.site.register(Customer)
admin.site.register(Service)
admin.site.register(Category)
admin.site.register(Branch)  
admin.site.register(Booking)

