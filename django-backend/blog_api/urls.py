from rest_framework.routers import DefaultRouter

from .views import PostView

app_name = "blog_api"
router = DefaultRouter()
router.register("", PostView, basename="post")
urlpatterns = router.urls
