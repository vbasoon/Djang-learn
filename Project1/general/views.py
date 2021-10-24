from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "general/index.html")

def about(request):
    return render(request, "general/about.html")

def contacts(request):
    return render(request, "general/contacts.html")

def greeting(request, name):
    return render(request, "general/greeting.html", {
        "name": name.capitalize()
    })

