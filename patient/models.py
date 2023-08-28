from django.db import models
from django.contrib.auth.models import User
from rules.file_uploader import image_uploader
# Create your models here.


class Patient(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    full_name = models.CharField(max_length=40, null=False, blank=False)
    phone = models.CharField(max_length=11, null=True, blank=False)
    age = models.IntegerField(null=True, blank=True, default=0)
    city = models.CharField(max_length=15, null=False, blank=False)
    description = models.TextField(max_length=1000)
    continuous_calculation = models.IntegerField(default=0)

    def __str__(self):
        return f"patient-name {self.full_name}, user_id {self.user.id} and user username {self.user.username}"


class Operation(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    patient = models.ForeignKey(Patient, null=False, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=15, null=False, blank=False)
    datetime = models.DateTimeField(auto_now=True)
    price = models.IntegerField(blank=False, null=False)
    description = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f"op_id {self.id}, op-name{self.name}, patient-name {self.patient.full_name}, username {self.user.username}"


class OperationImage(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to=image_uploader)


class Prescription(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    patient = models.ForeignKey(Patient, null=False, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.DO_NOTHING)
    datetime = models.DateTimeField(auto_now=True)
    medicine = models.TextField(max_length=500)

    def __str__(self):
        return f"Prescription_id {self.id} patient-name {self.patient.full_name}, username {self.user.username}"
