from django.urls import path
from .views import dr_nagib_cv

app_name = "accounts"

urlpatterns = [
    path('dr.mohamed-nagib', dr_nagib_cv, name="dr_nagib_cv")

]