from django.shortcuts import render, redirect
from .forms import TicketsForm, Ticket, BillingForm, Billing
from patient.models import Operation
from patient.models import Patient
from rules.help_function import get_date
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError


@login_required
def home(request, *args, **kwargs):
    form = TicketsForm(request.POST)
    queryset = Ticket.objects.filter(reservation_date=get_date())
    if request.method == 'POST':
        if form.is_valid():
            over_ride_form = form.save(commit=False)
            over_ride_form.user = request.user
            try:
                patient = get_object_or_404(Patient, id=form.cleaned_data['get_patient'])
                over_ride_form.patient = patient
                over_ride_form.save()
                return redirect(request.META['HTTP_REFERER'])
            except:
                form.add_error(None, "لا يوجد مريض بهذا الرقم التعريفي")

    else:
        form = TicketsForm()

    context = {
        "page_title": 'الرئيسية',
        'form': form,
        'tickets': queryset,
    }
    return render(request, 'home.html', context)


@login_required
def billing(request, *args, **kwargs):
    operation = get_object_or_404(Operation, id=kwargs['id'])
    billings = Billing.objects.filter(operation=operation)
    if request.method == 'POST':
        form = BillingForm(request.POST)
        if form.is_valid():
            over_ride_form = form.save(commit=False)
            over_ride_form.user = request.user
            over_ride_form.operation = operation
            if operation.remaining_amount >= over_ride_form.amount_paid and over_ride_form.amount_paid > 0:
                new_remaining_amount = int(operation.remaining_amount) - int(over_ride_form.amount_paid)
                over_ride_form.remaining_amount = new_remaining_amount
                over_ride_form.save()
                operation.remaining_amount = new_remaining_amount
                operation.save()
                return redirect(request.META['HTTP_REFERER'])

            elif operation.remaining_amount < over_ride_form.amount_paid:
                form.add_error(None, "تملأ هذه الخانة بسعر اقل او مساوي للمبلغ المتبقي")
                # raise ValidationError(" ")
            else:
                form.add_error(None, "تملأ هذه الخانة بسعر اقل او مساوي للمبلغ المتبقي واكبر من الصفر (قيمة موجبة)")
                # raise ValidationError(" ")
    else:
        form = BillingForm()
    context = {
        "page_title": f"اضافة فاتورة للعملية رقم {operation.id}",
        "operation": operation,
        "billings": billings,
        "form": form,
        "disable": operation.remaining_amount > 0,
    }

    return render(request, 'add_billing.html', context)


@login_required
def get_all_billing(request, *args, **kwargs):
    operation = get_object_or_404(Operation, id=kwargs['id'])
    billing = Billing.objects.filter(operation=operation)
    context = {
        "page_title": "فواتير العملية رقم " + f"{operation.id}",
        "billing": billing,
    }
    return render(request, 'operation_billing.html', context)

