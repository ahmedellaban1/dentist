from django import forms
from .models import Ticket, Billing
from rules.help_function import get_date


class TicketsForm(forms.ModelForm):
    get_patient = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['reservation_date'].initial = f"{get_date()}"

    class Meta:
        model = Ticket
        fields = ['get_patient', 'reservation_date', 'amount_paid', 'notes', 'examinationConsultation']

    def clean(self):
        cleaned_data = super().clean()
        get_patient = cleaned_data.get('get_patient')
        return cleaned_data

    def submit(self):
        get_patient = self.cleaned_data['get_patient']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['get_patient'].widget.attrs['placeholder'] = 'ادخل رقم المريض'
        self.fields['get_patient'].label = 'رقم المريض'

        self.fields['reservation_date'].label = 'تاريخ الحجز'
        self.fields['reservation_date'].dafult_value =''
        self.fields['reservation_date'].initial = f"{get_date()}"


        self.fields['amount_paid'].label =  "المبلغ المدفوع"
        self.fields['amount_paid'].dafult_value =''

        self.fields['notes'].label =  "ملاظات الاستقبال"
        self.fields['notes'].dafult_value =''

        self.fields['examinationConsultation'].label = " كشف / استشارة"
        self.fields['examinationConsultation'].dafult_value =''

