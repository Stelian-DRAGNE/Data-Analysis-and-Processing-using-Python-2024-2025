
from django.urls import path
from .views import random_view, alege_view


## URL MARE
urlpatterns = [
    path('random', random_view),
    path('alege/', alege_view),
]