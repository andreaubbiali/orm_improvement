from django.urls import path

from ecommerce.views.product_view import getProduct

urlpatterns = [
    path("", getProduct, name="getProduct"),
]