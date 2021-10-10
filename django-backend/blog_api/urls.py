from django.urls import path
from rest_framework.routers import DefaultRouter

from blog_api.views import AdminPostViewSet, PostViewSet, PostListDetailFilter

app_name = "blog_api"
router = DefaultRouter()
router.register("posts", PostViewSet, basename="post")
router.register("admin", AdminPostViewSet, basename="adminpost")
urlpatterns = [
    path("search/", PostListDetailFilter.as_view(), name="postsearch")
]

urlpatterns += router.urls
