from django.shortcuts import render



def home_page(request):
    templates = "home.html"
    return render(request, templates)