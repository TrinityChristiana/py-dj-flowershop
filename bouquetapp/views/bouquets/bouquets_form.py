from django.shortcuts import render

def add_bouquets(request):
    if request.method == "GET":
        template = "bouquets/bouquets_form.html"
        context = {}
        return render(request, template, context)

def edit_bouquets(request, bouquet_id):
    if request.method == "GET":
        template = "bouquets/bouquets_form.html"
        context = {}
        return render(request, template, context)
