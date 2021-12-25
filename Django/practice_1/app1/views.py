from django.shortcuts import render
from .models import Usuario


def index(request):
    santiago = Usuario(
        name='santiago',
        last_name='sola',
        email='santiagosolacosta@gmail.com',
    )
    return render(request, 'index.html', {'user':santiago})