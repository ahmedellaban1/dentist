from django.shortcuts import render, redirect
from .forms import AddPatientForm, Patient, Operation, AddOperationForm, AddOperationImage, OperationImage
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

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


def get_patient(request, *args, **kwargs):
    queryset = get_object_or_404(Patient, id=kwargs['id'], full_name=kwargs['full_name'])
    context = {
        "page_title": "معلومات المريض",
        "patient": queryset,
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
        "page_title": 'معلومات العملية',
        "form": form,
        'operation': operation,
        "images": images,
    }
    return render(request, 'operation_details.html', context)

@login_required
def edit_operation(request, *args, **kwargs):
    operation = get_object_or_404(Operation, id=kwargs['id'])
    if request.method == "POST":
        form = AddOperationForm(request.POST, instance=operation)
        if form.is_valid():
            form.save()
        return redirect('patient:operation_details', id=operation.patient.id, full_name=operation.patient.full_name, op_id=operation.id)

    else:
        form = AddOperationForm(instance=operation)

    context = {
        "page_title": "تعديل عملية",
        "form": form,
    }
    return render(request, 'edit_operation.html', context)
