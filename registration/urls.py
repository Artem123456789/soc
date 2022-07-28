from django.urls import path
from registration.views.registration_views import register

app_name = "registration"

urlpatterns = [
    path("register/", register)
]
