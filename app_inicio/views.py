from django.shortcuts import render

# Create your views here.

def AmaDGETI(request):
    return render(request, 'app_inicio/index.html')

def about(request):
    return render(request, 'app_inicio/about.html')

def sostenibles(request):
    return render(request, 'app_inicio/sostenibles.html')

def error(request):
    return render(request, 'app_inicio/error.html')