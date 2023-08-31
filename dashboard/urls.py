from django.urls import path
from .views import home, billing, get_all_billing

app_name = "dashboard"
urlpatterns = [
    path('', home, name='home'),
    path('billing/<int:id>', billing, name='billing'),
    path('operation_billing/<int:id>', get_all_billing, name='operation_billing'),
]