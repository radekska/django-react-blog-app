from users.models import NewUser
from django.db import models
from django.db.models.query import QuerySet
from strenum import StrEnum


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class StatusOptions(StrEnum):
    DRAFT = "Draft"
    PUBLISHED = "Published"


class Post(models.Model):
    class PostObjects(models.Manager):
        def get_queryset(self) -> QuerySet:
            return super().get_queryset().filter(status=StatusOptions.PUBLISHED.lower())

    status_options = (
        (StatusOptions.DRAFT.lower(), StatusOptions.DRAFT),
        (StatusOptions.PUBLISHED.lower(), StatusOptions.PUBLISHED),
    )

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=200)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=200, unique_for_date="published", blank=False, default=None)
    published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(NewUser, on_delete=models.CASCADE, related_name="blog_posts")
    status = models.CharField(max_length=10, choices=status_options, default="published")
    # Model Managers
    objects = models.Manager()
    post_objects = PostObjects()

    class Meta:
        ordering = ("-published",)

    def __str__(self) -> str:
        return self.title
