from django.shortcuts import render
from ..data_manager import get_all_bouquets

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
