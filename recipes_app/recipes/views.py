import random

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib import messages
from datetime import datetime, timedelta
import pytz
from django.views.generic.list import MultipleObjectMixin

from .models import Recipe, Ingredient


# Create your views here.


class HomeView(ListView):
    template_name = 'recipes/home.html'
    model = Recipe
    context_object_name = 'recipe_list'
    queryset = Recipe.objects.order_by('title')


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['title', 'description', 'portions', 'ingredients', 'steps', 'filters', 'image', 'recipe_ingredients']
    success_url = reverse_lazy('recipes:list_recipe')


class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    #  change the query done by django to something more custom
    queryset = Recipe.objects.order_by('title')
    #  replaces the object_list with recipe_list
    context_object_name = 'recipe_list'
    paginate_by = 10


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    fields = ['title', 'description', 'portions', 'ingredients', 'steps', 'filters', 'image']

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("recipes:detail_recipe", kwargs={"pk": pk})


class RecipeDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Recipe

    def get_success_url(self):
        return reverse("recipes:list_recipe")

    success_message = "Recipe deleted successfully"


class UserRecipesView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/user_recipes.html'
    queryset = Recipe.objects.order_by('title')

    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        context = super(UserRecipesView, self).get_context_data(*args, **kwargs)
        context["random_recipe"] = self.get_random_recipe()
        return context

    def get_queryset(self):
        return Recipe.objects.filter(user=self.request.user).all()

    def get_random_recipe(self):
        current_date = datetime.now(pytz.timezone('Europe/Amsterdam'))
        # tomorrow = current_date + timedelta(days=5)
        num_date_time = int(current_date.strftime('%d%m%Y'))
        recipes_list = Recipe.objects.filter(user=self.request.user).all()
        random.seed(num_date_time)
        if not recipes_list:
            return None

        random_recipe = random.choice(recipes_list)

        return random_recipe


@login_required
def add_recipe_to_account(request, pk):
    if request.POST:
        user = request.user
        recipe = Recipe.objects.get(pk=pk)

        if not user.recipes.filter(id=recipe.id):
            user.recipes.add(recipe)
            user.save()

            messages.success(request, "Recipe added successfully")
        else:
            messages.warning(request, "Recipe already in your account")

        return HttpResponseRedirect(reverse('recipes:list_recipe'))


@login_required
def delete_recipe_from_account(request, pk):
    if request.POST:
        recipe = Recipe.objects.get(pk=pk)
        user = request.user
        user.recipes.remove(recipe)
        messages.success(request, "Recipe deleted successfully")

        return HttpResponseRedirect(reverse('recipes:user_recipes'))


class IngredientListView(LoginRequiredMixin, ListView):
    model = Ingredient
    #  change the query done by django to something more custom
    queryset = Ingredient.objects.order_by('name')
    context_object_name = 'ingredient_list'
    paginate_by = 10


class IngredientCreateView(LoginRequiredMixin, CreateView):
    model = Ingredient
    fields = '__all__'
    success_url = reverse_lazy('recipes:list_ingredient')


class IngredientUpdateView(LoginRequiredMixin, UpdateView):
    model = Ingredient
    fields = '__all__'
    success_url = reverse_lazy('recipes:list_ingredient')


class IngredientDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Ingredient

    def get_success_url(self):
        return reverse("recipes:list_ingredient")

    success_message = "Ingredient deleted successfully"
