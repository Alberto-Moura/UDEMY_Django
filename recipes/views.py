from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Estamos na Home!")


def contato(request):
    return HttpResponse("Estamos em Contato!")


def sobre(request):
    return HttpResponse("Estamos em Sobre!")
