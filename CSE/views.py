from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def aboutus(request):
    return render(request,'aboutus.html')
def contact(request):
    return render(request,'contact.html')
def products(request):
    return render(request,'products.html')
def service(request):
    return render(request,'service.html')
#if we scribble something in the system we call it render