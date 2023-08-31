from django.urls import path
from .views import home, billing

app_name = "dashboard"
urlpatterns = [
    path('', home, name='home'),
    path('billing/<int:id>', billing, name='billing'),
]