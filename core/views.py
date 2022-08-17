from django.shortcuts import render, HttpResponse

html_base = """
<h1>Mi web personal</h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about-me/">Acerca de</a></li>
    
</ul>
"""


def home(request):
    return HttpResponse(html_base + "<h2>Portada</h2")


def about(request):
    return HttpResponse(html_base+"<h2>Acerca de</h2><p>Me llamo Maria y soy programadora</p>")