from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'manager_inventory/pages/index.html')


def home(request):
    return render(request, 'manager_inventory/pages/home.html')


def estoque(request):
    return render(request, 'manager_inventory/pages/estoque.html')


def categoria(request):
    return render(request, 'manager_inventory/pages/categoria.html')
