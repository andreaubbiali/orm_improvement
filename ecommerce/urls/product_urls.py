from django.urls import path

from ecommerce.views.product_views import getProduct

urlpatterns = [
    path("", getProduct, name="getProduct"),
]