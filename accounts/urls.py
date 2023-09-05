from django.urls import path
from .views import dr_nagib_cv, about_developer

app_name = "accounts"

urlpatterns = [
    path('dr.mohamed-nagib', dr_nagib_cv, name="dr_nagib_cv"),
    path('about_developer', about_developer, name="about_developer")

]