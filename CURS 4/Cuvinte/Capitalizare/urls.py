
from django.urls import path
from .views import capitalizare_view, parametri_view



## URL MIC
urlpatterns = [
    path('parametri/', parametri_view),
    path('<text>', capitalizare_view),
]