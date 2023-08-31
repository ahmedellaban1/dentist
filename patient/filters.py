import django_filters
from .models import Patient


class PatientFilter(django_filters.FilterSet):
    full_name = django_filters.CharFilter(lookup_expr='icontains')
    phone = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Patient
        fields = ['id', 'full_name', 'phone']

