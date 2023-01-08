from django.urls import path
from . import views

urlpatterns = [
    path('',views.sci_homepage),
    path('biology/',views.bio),
    path('chemistry/',views.chem),
    path('physics/',views.phy)
]