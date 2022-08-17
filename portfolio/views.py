from django.shortcuts import render
from .models import Project


# Create your views here.
def portfolio(request):
    kw = {'projects': Project.objects.all()}  # Devuelve toda la lista de proyectos
    return render(request, "portfolio/portfolio.html",kw)
