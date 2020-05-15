from django.urls import path
from .views import *

app_name = "bouquetapp"

urlpatterns = [
    path("", list_bouquets, name="bouquets"),
    path("bouquet/<int:bouquet_id>", details_bouquets, name="bouquet")
]
