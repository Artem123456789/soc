from rest_framework import routers
from comments.views.comments_views import CommentsViewSet

router = routers.DefaultRouter
router.register("comments", CommentsViewSet)
urlpatterns = router.urls
