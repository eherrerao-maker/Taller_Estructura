from django.shortcuts import render

# Create your views here.


def presentarinformacion(request):
    data = {
        'nombre': 'Elian Herrera Omedo',
        'marca': 'Hadami',
        'descripcion': 'Hadami es una marca ficticia de ropa personalizada enfocada en diseño minimalista y calidad artesanal.',
        'version': '1.0',
        'productos': [
            {'titulo': 'Camiseta Hadami — Minimal', 'precio': '$25', 'descripcion': 'Corte cómodo, logo bordado.'},
            {'titulo': 'Sudadera Hadami — Urban', 'precio': '$45', 'descripcion': 'Algodón premium, capucha ajustable.'},
            {'titulo': 'Gorra Hadami — Classic', 'precio': '$18', 'descripcion': 'Visera curva, logo frontal.'},
        ],
    }
    return render(request, 'base.html', data)