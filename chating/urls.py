from rest_framework.routers import DefaultRouter
from chating.views.chating_views import ChatingViewSet

app_name = "chating"

router = DefaultRouter()
router.register(r"chating", ChatingViewSet)
urlpatterns = router.get_urls()
