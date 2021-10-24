from django.shortcuts import render

# Create your views here.
def index(request):
    age = 18
    return render(request, "adult/index.html", {
        "age": True
    })
