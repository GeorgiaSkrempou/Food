from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Recipe


# Create your views here.


class HomeView(TemplateView):
    template_name = 'recipes/home.html'


class ThankYouView(TemplateView):
    template_name = 'recipes/thank_you.html'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    # attribute names must be named like this
    model = Recipe
    # the form details are automatically saved like this
    fields = '__all__'
    #  success url? # it's the url not the template!
    success_url = reverse_lazy('recipes:list_recipe')


# This lists every instance of the teacher
# model_list.hmtl
class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    #  change the query done by django to something more custom
    queryset = Recipe.objects.order_by('title')
    #  replaces the object_list with recipe_list
    context_object_name = 'recipe_list'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    fields = "__all__"

    # success_url = reverse_lazy('recipes:detail_recipe', args = [recipe.id])

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("recipes:detail_recipe", kwargs={"pk": pk})


class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe

    # success_url = reverse_lazy("recipes:list_recipe")

    def get_success_url(self):
        return reverse("recipes:list_recipe")
