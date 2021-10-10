from django.urls import path
from rest_framework.routers import DefaultRouter

from blog_api.views import PostView, PostListDetailFilter

app_name = "blog_api"
router = DefaultRouter()
router.register("posts", PostView, basename="post")
urlpatterns = [
    path("search/", PostListDetailFilter.as_view(), name="postsearch")
]

urlpatterns += router.urls
