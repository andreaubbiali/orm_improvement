from django.urls import path

from ecommerce.views.user import register_user

urlpatterns = [
    path("register/", register_user, name="register_user"),
]