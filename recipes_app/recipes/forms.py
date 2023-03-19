from django import forms
from django.forms.models import inlineformset_factory

from .models import Recipe, RecipeIngredient


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ('user', 'ingredients', "total_calories")


IngredientFormSet = inlineformset_factory(Recipe, RecipeIngredient, form=RecipeForm, extra=1)
