from django.shortcuts import render, redirect
from .forms import TicketsForm, Ticket
from patient.models import Patient
from rules.help_function import get_date
from django.shortcuts import get_object_or_404


def home(request, *args, **kwargs):
    form = TicketsForm(request.POST)
    queryset = Ticket.objects.filter(date=get_date())
    if request.method == 'POST':
        if form.is_valid():
            over_ride_form = form.save(commit=False)
            over_ride_form.user = request.user
            over_ride_form.patient = get_object_or_404(Patient, id=form.cleaned_data['get_patient'])
            over_ride_form.save()
        return redirect(request.META['HTTP_REFERER'])
    else:
        form = TicketsForm()

    context = {
        "page_title": 'Home',
        'form': form,
        'tickets': queryset,
    }
    return render(request, 'home.html', context)
