from django.urls import path
from .views import *

app_name = "bouquetapp"

urlpatterns = [
    path("", list_bouquets, name="bouquets")
]
