from django.shortcuts import render, redirect
from .forms import (AddPatientForm, Patient, Operation, AddOperationForm,
                    AddOperationImage, OperationImage, PrescriptionForm,
                    EditOperationForm, Prescription, EditPatientForm, )
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .filters import PatientFilter

# Create your views here.

@login_required
def add_patient(request, *args, **kwargs):
    form = AddPatientForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            over_ride_form = form.save(commit=False)
            over_ride_form.user = request.user
            over_ride_form.save()
            return redirect('patient:patient_details', id=over_ride_form.id, full_name=over_ride_form.full_name)
    else:
        form = AddPatientForm()

    context = {
        "page_title": 'إضافة مريض جديد',
        "form": form,

    }
    return render(request, 'add_patient.html', context)


@login_required
def get_patient(request, *args, **kwargs):
    queryset = get_object_or_404(Patient, id=kwargs['id'], full_name=kwargs['full_name'])
    all_operation = Operation.objects.filter(patient=queryset)
    total_remaining_amount = 0
    for i in all_operation:
        total_remaining_amount += i.remaining_amount

    context = {
        "page_title": "معلومات المريض"+f" ( {queryset.id} )",
        "patient": queryset,
        "total_remaining_amount": total_remaining_amount,
    }
    return render(request, 'profile-details.html', context)

@login_required
def add_operation(request, *args, **kwargs):
    form = AddOperationForm(request.POST)
    patient = get_object_or_404(Patient, id=kwargs['id'], full_name=kwargs['full_name'])
    all_operation = Operation.objects.filter(patient=patient)
    if request.method == 'POST':
        if form.is_valid():
            over_ride_form = form.save(commit=False)
            over_ride_form.user = request.user
            over_ride_form.patient = patient
            over_ride_form.remaining_amount = over_ride_form.price
            over_ride_form.save()
            return redirect(request.META['HTTP_REFERER'])
    else:
        form = AddOperationForm()
    context = {
        "page_title": 'إضافة عملية',
        "form": form,
        "operations": all_operation,
        "patient": patient
    }
    return render(request, 'add_operation.html', context)

@login_required
def operation_details(request, *args, **kwargs):
    form = AddOperationImage(request.POST, request.FILES)
    operation = Operation.objects.get(id=kwargs['op_id'])
    images = OperationImage.objects.filter(operation=operation)
    if request.method == 'POST':
        if form.is_valid():
            over_ride_form = form.save(commit=False)
            over_ride_form.user = request.user
            over_ride_form.operation = operation
            over_ride_form.save()
            return redirect(request.META['HTTP_REFERER'])
    else:
        form = AddOperationImage()
    context = {
        "page_title": 'معلومات العملية'+f"( {operation.id} )",
        "form": form,
        'operation': operation,
        "images": images,
    }
    return render(request, 'operation_details.html', context)

@login_required
def edit_operation(request, *args, **kwargs):
    operation = get_object_or_404(Operation, id=kwargs['id'])
    if request.method == "POST":
        form = EditOperationForm(request.POST, instance=operation)
        if form.is_valid():
            form.save()
        return redirect('patient:operation_details', id=operation.patient.id, full_name=operation.patient.full_name, op_id=operation.id)

    else:
        form = EditOperationForm(instance=operation)

    context = {
        "page_title": f"تعديل عملية {operation.id}",
        "form": form,
    }
    return render(request, 'edit_operation.html', context)


@login_required
def edit_patient(request, *args, **kwargs):
    patient = get_object_or_404(Patient, id=kwargs['id'], full_name=kwargs['full_name'])
    if request.method == "POST":
        form = EditPatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
        return redirect('patient:patient_details', id=patient.id, full_name=patient.full_name)

    else:
        form = EditPatientForm(instance=patient)

    context = {
        "page_title": f"تعديل مريض رقم {patient.id}",
        "form": form,
    }
    return render(request, 'edit_patient.html', context)


@login_required
def search_patient(request, *args, **kwargs):
    your_model_filter = PatientFilter(request.GET, queryset=Patient.objects.all())
    filtered_queryset = your_model_filter.qs

    if not any(request.GET.values()):
        filtered_queryset = Patient.objects.none()

    context = {
        "page_title": "بحث",
        'filter': your_model_filter,
        'filtered_queryset': filtered_queryset
    }

    return render(request, 'search_patient.html', context)


@login_required
def add_prescription(request, *args, **kwargs):
    form = PrescriptionForm(request.POST)
    patient = get_object_or_404(Patient, id=kwargs['id'], full_name=kwargs['full_name'])
    operation = get_object_or_404(Operation, id=kwargs['op_id'], patient=patient)
    prescriptions = Prescription.objects.filter(operation=operation)
    if request.method == 'POST':
        if form.is_valid():
            over_ride_form = form.save(commit=False)
            over_ride_form.user = request.user
            over_ride_form.patient = patient
            over_ride_form.operation = operation
            over_ride_form.save()
            instance = Prescription.objects.filter(patient=patient, operation=operation).last()
            return redirect('patient:get_prescription', id=instance.id)
            # return redirect(request.META['HTTP_REFERER'])
    else:
        form = PrescriptionForm()
    context = {
        "page_title": 'إضافة روشتة',
        "form": form,
        "operation": operation,
        "patient": patient,
        "prescriptions": prescriptions,
    }
    return render(request, 'add_prescription.html', context)


@login_required
def get_prescription(request, *args, **kwargs):
    prescription = get_object_or_404(Prescription, id=kwargs['id'])
    context = {
        "prescription": prescription,
    }
    return render(request, 'get_prescription.html', context)

@login_required
def get_all_prescription(request, *args, **kwargs):
    patient = get_object_or_404(Patient, id=kwargs['id'])
    all_prescriptions = Prescription.objects.filter(patient=patient)
    context = {
        "page_title": "الادوية",
        "all_prescriptions": all_prescriptions,
    }
    return render(request, 'all_prescriptions.html', context)


@login_required
def get_operations_done(request, *args, **kwargs):
    operations = Operation.objects.filter(patient_id=kwargs['id'], remaining_amount=0)
    context = {
        "page_title": "العمليات التامة",
        "operations": operations,
    }
    return render(request, 'done_operations.html', context)
