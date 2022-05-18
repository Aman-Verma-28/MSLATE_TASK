
from django.urls import path, include
from .views import index, getRank

urlpatterns = [
    path('', index, name="index"),
    path('rank/', getRank),
]
