from django.urls import path
from .views import inicio_tienda

urlpatterns = [
    path('', inicio_tienda, name='tienda'),
]