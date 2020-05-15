from django.shortcuts import render

def details_bouquets(request, bouquet_id):
    """
    This view handels all request to the bouquets details page
    url_ex: bouquet/1
    """
    if request.method == "GET":
        template = "bouquets/bouquets_details.html"
        context = {}
        return render(request, template, context)
