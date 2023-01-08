from django.urls import path
from . import views

urlpatterns = [
    path('algebra/',views.algebra),
    path('geometry/',views.geometry)
]