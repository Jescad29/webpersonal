from django.shortcuts import render, HttpResponse

html_base = """
<h1>Mi web personal</h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about">Acerca de</a></li>
</ul>
"""

# Create your views here.


def home(request):
    return HttpResponse(html_base + """
        <h2>Portada</h2>
        <p>Esto es la portada</p>
    """)


def about(request):
    return HttpResponse(html_base + """
        <h2>Acerca de</h2>
        <p>Me llamo Jesus y soy desarrollador backend</p>
    """)
