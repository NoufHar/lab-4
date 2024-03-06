from django.shortcuts import render
from django.http import HttpResponse
tax_rate = 0.15

# Create your views here.
def Default(request):
    return HttpResponse(" this is a site to calculate tax.")

def anyNumber(request , num ):
    totalPrice = num + (num * tax_rate)
    return HttpResponse(f"<h1>the total price after 15% tax :  , {totalPrice}</h>")

def taxrate(request):
    return render(request, 'Taxapp/tax_rate.html' , {'tax rate' : tax_rate} )