from django.shortcuts import render

def list_bouquets(request):
    if request.method == "GET":
        template = "bouquets/bouquets_list.html"
        context = {}
        return render(request, template, context)
