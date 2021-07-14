from django import http
from django.http import HttpResponse
import datetime

#Vista 1
def saludo(request): 
    respuesta = """<html>
    <body>
    <h1>
    Hola Santi
    </h1>
    </body>
    </html>"""
    return HttpResponse(respuesta)

#Vista 2
def despedida(request): 
    return HttpResponse("Nos vemos Santi")

#Vista 3
def fecha(request): 
    fecha_actual = datetime.datetime.now()
    respuesta = f"""<html>
    <body>
    <h2>
    La Fecha y hora actual es: {fecha_actual} 
    </h2>
    </body>
    </html>"""
    return HttpResponse(respuesta)

#Vista 4
def calcularedad(request, edad, age):
    periodo = age - 2021
    edadfutura = edad + periodo
    respuesta = f"""<html>
    <body>
    <h2>
    La edad que tendria en {age} seria de {edadfutura} años
    </h2>
    </body>
    </html>"""
    return HttpResponse(respuesta)