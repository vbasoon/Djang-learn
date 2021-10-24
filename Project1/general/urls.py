from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about),
    path("contacts", views.contacts),
    path("<str:name>", views.greeting, name="greeting"),

]