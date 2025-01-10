from django.shortcuts import render

# Create your views here.

def Pag(request):
    return render(request,'PaginaDeInicio.html')