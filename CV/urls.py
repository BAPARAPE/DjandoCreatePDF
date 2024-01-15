from django.urls import path

from CV.views import index, formulaire, verification

urlpatterns = [
    path('', index, name="accueil"),
    path('creercv', formulaire, name="creer"),
    path('verification', verification, name="verification")
]