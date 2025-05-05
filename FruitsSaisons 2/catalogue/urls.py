from django.urls import path
from . import views

urlpatterns = [
    path('', views.acceuil, name='acceuil'),
    path('gestion/', views.gestion_saisons, name='gestion_saisons'),
    path('affichage/', views.afficher_saisons, name='afficher_saisons'),
    path('saison/supprimer/<int:saison_id>/', views.supprimer_saison, name='supprimer_saison'),
    path('fruit/supprimer/<int:fruit_id>/', views.supprimer_fruit, name='supprimer_fruit'),
]