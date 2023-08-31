from django.urls import path
from .views import add_patient, get_patient, add_operation, operation_details, edit_operation

app_name = "patient"
urlpatterns = [
    path('add_patient', add_patient, name='add_patient'),
    path('patient_details/<int:id>-<str:full_name>', get_patient, name='patient_details'),
    path('patient_details/operations/<int:id>-<str:full_name>', add_operation, name='add_operation'),
    path('patient_details/operations/<int:id>-<str:full_name>/<int:op_id>', operation_details, name='operation_details'),
    path('patient_details/operations/edit_operation/<int:id>', edit_operation, name='edit_operation'),
]
