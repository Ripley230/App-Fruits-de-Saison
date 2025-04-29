from django.shortcuts import render, redirect, get_object_or_404
from .models import Saison, Fruit
from .forms import SaisonForm, FruitForm

# PAGE 1 : Permet de créer ou modifier les saisons et ajouter des fruits
def gestion_saisons(request):
    saisons = Saison.objects.all()
    fruits = Fruit.objects.all()

    # Saison
    saison_form = SaisonForm(request.POST or None, prefix='saison')
    if saison_form.is_valid():
        saison_form.save()
        return redirect('gestion_saisons')

    # Fruit
    fruit_form = FruitForm(request.POST or None, prefix='fruit')
    if fruit_form.is_valid():
        fruit_form.save()
        return redirect('gestion_saisons')

    context = {
        'saisons': saisons,
        'fruits': fruits,
        'saison_form': saison_form,
        'fruit_form': fruit_form,
    }
    return render(request, 'catalogue/gestion_saisons.html', context)

# PAGE 2 : Afficher les données
def afficher_saisons(request):
    saisons = Saison.objects.prefetch_related('fruits').all()
    return render(request, 'catalogue/afficher_saisons.html', {'saisons': saisons})

def acceuil(request):
    return render(request, 'catalogue/acceuil.html')

def supprimer_saison(request, saison_id):
    saison = get_object_or_404(Saison, id=saison_id)
    saison.delete()
    return redirect('gestion_saisons')

def supprimer_fruit(request, fruit_id):
    fruit = get_object_or_404(Fruit, id=fruit_id)
    fruit.delete()
    return redirect('gestion_saisons')