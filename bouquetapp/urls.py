from django.urls import path
from .views import *

app_name = "bouquetapp"

urlpatterns = [
    path("", list_bouquets, name="bouquets"),
    path("bouquet/<int:bouquet_id>", details_bouquets, name="bouquet"),
    path("bouquet/form", add_bouquets, name="bouquet_form"),
    path("bouquet/<int:bouquet_id>/form", edit_bouquets, name="bouquet_edit"),
]
