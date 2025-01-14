from django.urls import path

from ecommerce.views.user_view import register_user

urlpatterns = [
    path("register/", register_user, name="register_user"),
]