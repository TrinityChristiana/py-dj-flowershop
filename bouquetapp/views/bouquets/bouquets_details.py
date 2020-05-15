from django.shortcuts import render, redirect, reverse
from ..data_manager import *

def details_bouquets(request, bouquet_id):
    """
    This view handels all request to the bouquets details page
    url_ex: bouquet/1
    """
    if request.method == "GET":
        template = "bouquets/bouquets_details.html"
        bouquet = get_bouquet(bouquet_id)
        bouquet_flowers = get_relations(bouquet_id)
        context = {
            "bouquet": bouquet,
            "bouquet_flowers": bouquet_flowers
        }
        return render(request, template, context)
    elif request.method == "POST":
        form_data = request.POST

        if "actual_method" in form_data and form_data["actual_method"] == "PUT":
            update_bouquet(form_data, bouquet_id)
            return redirect("bouquetapp:bouquet", bouquet_id=bouquet_id)

