from django.shortcuts import render, HttpResponse

html_base = """
<h1>Mi web personal</h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about-me/">Acerca de</a></li>
    <li><a href="/portfolio/">Portafolio</a></li>
    <li><a href="/contact/">Contacto</a></li>
    
</ul>
"""


def home(request):
    return render(request, "core/home.html")

def about(request):
    return HttpResponse(html_base + """
        <h2>Acerca de</h2>
        <p>Me llamo Maria y soy programadora</p>
    """)


def portfolio(request):
    return HttpResponse(html_base + """
        <h2>Portafolio</h2>
        <p>Algunos de mis trabajos</p>
    """)


def contact(request):
    return HttpResponse(html_base + """
        <h2>Contacto</h2>
        <p>Aquí les comparto mi email para preguntarme dudas: <a href="maito:correo@test.com">correo@test.com</a></p>
    """)
