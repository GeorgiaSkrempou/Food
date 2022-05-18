from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy


from .forms import NewRecipeForm

# Create your views here.


class ThankYouView(TemplateView):
    template_name = 'recipes/thank_you.html'


class RecipeFormView(FormView):
    # attribute names must be named like this
    form_class = NewRecipeForm
    template_name = 'recipes/new_recipe.html'

    #  success url? # it's the url not the template!
    success_url = reverse_lazy('recipes:thank_you')

    #  what to do with form?
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
