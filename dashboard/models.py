from django.db import models
from patient.models import Patient, User, Operation
from rules.choices import TICKET_TYPE


# Create your models here.


class Ticket(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    patient = models.ForeignKey(Patient, null=False, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.DO_NOTHING)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    reservation_date = models.DateField(auto_created=True)
    amount_paid = models.IntegerField(null=False, blank=False, default=0)
    notes = models.TextField(max_length=100)
    examinationConsultation = models.CharField(max_length=12, choices=TICKET_TYPE, default=TICKET_TYPE[0][0])

    def __str__(self):
        return f" {self.id} user {self.user.username}, patient {self.patient.full_name}"


class Billing(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.DO_NOTHING)
    datetime = models.DateTimeField(auto_now=True)
    amount_paid = models.IntegerField(null=False, blank=False, default=0)
    remaining_amount = models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return f" user {self.user.username}, patient {self.operation.name}"
