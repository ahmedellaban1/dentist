from django.contrib import admin
from .models import Operation, Patient, OperationImage, Prescription
# Register your models here.

admin.site.register(Operation)
admin.site.register(Patient)
admin.site.register(OperationImage)
admin.site.register(Prescription)
