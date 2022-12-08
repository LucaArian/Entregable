from django.shortcuts import render
from django.http import HttpResponse
from .models import familiar

def mostrar():
    fam1= familiar(nombre="Adriana Moyano", edad= 49, fecha="1973-4-17")
    muestra1= f"Sus datos son: nombre: {fam1.nombre}, edad: {fam1.edad}, nacimiento: {fam1.fecha}"
    fam2= familiar(nombre="Luana Bartonek", edad= 18, fecha="2003-12-17")
    muestra2= f"Sus datos son: nombre: {fam2.nombre}, edad: {fam2.edad}, nacimiento: {fam2.fecha}"
    fam3= familiar(nombre="Sergio Bartonek", edad= 46, fecha="1977-7-8")
    muestra3= f"Sus datos son: nombre: {fam3.nombre}, edad: {fam3.edad}, nacimiento: {fam3.fecha}"
    return HttpResponse(muestra1, muestra2, muestra3)
# Create your views here.
