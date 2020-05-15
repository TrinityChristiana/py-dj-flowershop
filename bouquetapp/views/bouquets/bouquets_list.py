from django.shortcuts import render
from ..data_manager import get_all_bouquets

def list_bouquets(request):
    if request.method == "GET":
        bouquets = get_all_bouquets()
        template = "bouquets/bouquets_list.html"
        context = {
            "bouquets": bouquets
        }
        return render(request, template, context)
