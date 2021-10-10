from typing import Any

from blog.models import Post
from django.db.models import QuerySet
from rest_framework import filters, generics, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import BasePermission, IsAdminUser, IsAuthenticated, SAFE_METHODS
from rest_framework.request import Request

from .serializers import PostSerializer


class PostUserWritePermission(BasePermission):
    message = "Editing post is restricted to author only."

    def has_object_permission(self, request: Request, view, obj) -> bool:
        if request.method in SAFE_METHODS:
            return True
        return request.user == obj.author


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (PostUserWritePermission, IsAuthenticated)
    serializer_class = PostSerializer

    def get_queryset(self) -> QuerySet:
        user = self.request.user
        return Post.objects.filter(author=user)

    def get_object(self, **kwargs: Any) -> Post:
        item = self.kwargs.get("pk")
        try:
            item = int(item)
        except ValueError:
            return get_object_or_404(Post, slug=item)
        return get_object_or_404(Post, id=item)


class AdminPostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    serializer_class = PostSerializer

    def get_queryset(self) -> QuerySet:
        return Post.objects.all()


class PostListDetailFilter(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ("^slug", "^title")
