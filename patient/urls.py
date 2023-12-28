from django.urls import path
from .views import (add_patient, get_patient, add_operation,
                    operation_details, edit_operation,
                    search_patient, add_prescription, get_prescription, get_all_prescription, edit_patient,
                    get_operations_done, )

app_name = "patient"
urlpatterns = [
    path('add_patient', add_patient, name='add_patient'),
    path('search', search_patient, name='search'),
    path('patient_details/<int:id>-<str:full_name>', get_patient, name='patient_details'),
    path('patient_details/edit_patient/<int:id>-<str:full_name>', edit_patient, name='edit_patient'),
    path('patient_details/operations/<int:id>-<str:full_name>', add_operation, name='add_operation'),
    path('patient_details/operations/get_operations_done/<int:id>', get_operations_done, name='get_operations_done'),
    path('patient_details/operations/<int:id>-<str:full_name>/<int:op_id>', operation_details, name='operation_details'),
    path('patient_details/operations/edit_operation/<int:id>', edit_operation, name='edit_operation'),
    path('patient_details/operations/add_prescription/<int:id>-<int:op_id>-<str:full_name>', add_prescription, name='add_prescription'),
    path('patient_details/operations/get_prescription/<int:id>', get_prescription, name='get_prescription'),
    path('patient_details/operations/get_all_prescription/<int:id>', get_all_prescription, name='get_all_prescription'),
]
