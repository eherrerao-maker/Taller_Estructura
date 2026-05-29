from django.urls import path
from .views import presentarinformacion

urlpatterns = [
    path('', presentarinformacion, name='inicio'),
]