from rest_framework import routers
from posts.views import posts_views

app_name = "posts"

router = routers.DefaultRouter()
router.register("posts", posts_views.PostsViewSet)
urlpatterns = router.get_urls()
