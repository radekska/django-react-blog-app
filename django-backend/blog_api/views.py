from typing import Any

from blog.models import Post
from django.db.models import QuerySet
from rest_framework import status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import PostSerializer


class PostUserWritePermission(BasePermission):
    message = "Editing post is restricted to author only."

    def has_object_permission(self, request: Request, view, obj) -> bool:
        if request.method in SAFE_METHODS:
            return True

        return request.user == obj.author


class PostView(viewsets.ModelViewSet):
    permission_classes = [PostUserWritePermission]
    serializer_class = PostSerializer

    @property
    def queryset(self) -> QuerySet:
        return Post.post_objects.all()

    def get_object(self, queryset: QuerySet = None, **kwargs: Any) -> Post:
        item = self.kwargs.get("pk")
        try:
            item = int(item)
        except ValueError:
            return get_object_or_404(Post, slug=item)
        return get_object_or_404(Post, id=item)

# ViewSet implementation for PostView #
# The base ViewSet class does not provide any actions by default.
# class PostView(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]
#
#     @property
#     def queryset(self) -> QuerySet:
#         return Post.post_objects.all()
#
#     def list(self, request: Request) -> Response:
#         serializer = PostSerializer(self.queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request: Request, pk: int = None) -> Response:
#         post = get_object_or_404(self.queryset, pk=pk)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#
#     @staticmethod
#     def create(request: Request):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             post = Post.objects.create(**serializer.validated_data)
#             post.save()
#             return Response(status=status.HTTP_201_CREATED)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def update(self, request: Request, pk: int = None):
#         pass
#
#     def partial_update(self, request: Request, pk: int = None):
#         pass
#
#     def destroy(self, request, pk=None):
#         pass
