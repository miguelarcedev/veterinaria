
from django.shortcuts import render

def index(request):
   
    return render(request, "index.html")

def identidad(request):
   
    return render(request, "identidad.html")

def filosofia(request):
   
    return render(request, "filosofia.html")

def foda(request):
   
    return render(request, "foda.html")

def indicadores(request):
   
    return render(request, "indicadores.html")

def staff(request):
   
    return render(request, "staff_grid.html")