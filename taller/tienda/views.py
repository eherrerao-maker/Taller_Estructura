from django.shortcuts import render

# Create your views here.

def inicio_tienda(request):
    context = {
        'nombre': 'Elian Herrera Omedo',
        'marca': 'Hadami',
        'descripcion': 'Tienda Hadami — próximamente más productos.',
        'productos': []
    }
    return render(request, 'base.html', context)