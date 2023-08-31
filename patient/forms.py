from django import forms
from .models import Patient, Operation, OperationImage


class AddPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['full_name', 'phone', 'age', 'city', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].label = 'اسم المريض'

        self.fields['phone'].label = 'رقم المهاتف'

        self.fields['age'].label = "العمر"

        self.fields['city'].label = "البلد"

        self.fields['description'].label = "وصف حالة المريض او اي امراض متعلقة"


class AddOperationForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = ['name', 'price', 'description']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'اسم العملية'

        self.fields['price'].label = 'سعر العملية'

        self.fields['description'].label = "الوصف "


class AddOperationImage(forms.ModelForm):
    class Meta:
        model = OperationImage
        fields = ['image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].label = ''
