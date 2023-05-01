from django.contrib import admin
from .models import Patient, Clinic

# Register your models here.
admin.site.register(Patient)
admin.site.register(Clinic)