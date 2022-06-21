from django import forms
from django.forms.models import inlineformset_factory

from .models import Recipe, RecipeIngredient


class RecipeForm(forms.ModelForm):
    # quantity = forms.FloatField()
    # unit = forms.CharField(max_length=30)

    class Meta:
        model = Recipe
        exclude = ('user', 'ingredients',)


IngredientFormSet = inlineformset_factory(Recipe, RecipeIngredient, form=RecipeForm, extra=1)
