from chating.views.chating_views import send_message
from django.urls import path

app_name = "chating"

urlpatterns = [
    path("send_message/", send_message)
]
