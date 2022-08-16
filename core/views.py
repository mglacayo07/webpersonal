from django.shortcuts import render, HttpResponse


def home(request):
    html_response = "<h1>Mi web personal</h1>"
    for i in range(10):
        html_response += "<h2>Portada</h2>"
    return HttpResponse(html_response)
