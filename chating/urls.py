from chating.views.chating_views import send_message, get_chat
from django.urls import path

app_name = "chating"

urlpatterns = [
    path("send_message/", send_message),
    path("get_chat/", get_chat)
]
