from django import forms
from .models import Fruit, Saison

class SaisonForm(forms.ModelForm):
    class Meta:
        model = Saison
        fields = '__all__'

class FruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'