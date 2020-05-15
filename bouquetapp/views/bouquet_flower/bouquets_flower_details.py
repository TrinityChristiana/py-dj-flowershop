from django.shortcuts import render, redirect, reverse
from ..data_manager import *

def details_bouquets_flower(request, bouquets_flower_id, bouquet_id):
    """
    This view handels only POST request for bouquets_flower
    """
    if request.method == "POST":
        form_data = request.POST
        if "actual_method" in form_data and form_data["actual_method"] == "DELETE":
            remove_relation(bouquets_flower_id)

            return redirect("bouquetapp:bouquet", bouquet_id=bouquet_id)

