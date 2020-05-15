from django.shortcuts import render, reverse, redirect
from ..data_manager import *

def list_bouquets(request):
    """
    This view handles all request to the list of bouquet page
    url_ex: /
    """
    if request.method == "GET":
        bouquets = get_all_bouquets()
        template = "bouquets/bouquets_list.html"
        context = {
            "bouquets": bouquets
        }
        return render(request, template, context)
    elif request.method == "POST":
        form_data = request.POST
        add_bouquet(form_data)
        return redirect(reverse("bouquetapp:bouquets"))



