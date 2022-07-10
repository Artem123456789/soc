from rest_framework import routers
from registration.views.registration_views import RegistrationViewSet

app_name = "registration"

router = routers.DefaultRouter()
router.register("registration", RegistrationViewSet)

urlpatterns = router.urls
