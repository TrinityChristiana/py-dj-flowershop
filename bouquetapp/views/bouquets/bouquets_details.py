from django.shortcuts import render

def details_bouquets(request, bouquet_id):
    if request.method == "GET":
        template = "bouquets/bouquets_details.html"
        context = {}
        return render(request, template, context)
