from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "category", "title", "image", "slug", "author",
                  "excerpt", "content", "status")
        read_only_fields = ("published", "status")
        extra_fields = {"published": {"required": False}}
        validators = []  # Remove a default "unique together" constraint.
