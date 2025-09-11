from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context = {"name": "Theo Dal Pozzo"}
    return render(request, "core/home.html", context)
