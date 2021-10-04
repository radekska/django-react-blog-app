from django.urls import path
from .views import BlacklistTokenView, CustomUserCreate

app_name = "users"

urlpatterns = [
    path("register/", CustomUserCreate.as_view(), name="create_user"),
    path("logut/blacklist/", BlacklistTokenView.as_view(), name="blacklist")
]
