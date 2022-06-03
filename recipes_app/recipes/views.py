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

from .models import Recipe


# Create your views here.


class HomeView(TemplateView):
    template_name = 'recipes/home.html'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    # attribute names must be named like this
    model = Recipe
    # the form details are automatically saved like this
    fields = ['title', 'description', 'portions', 'ingredients', 'steps', 'filters']
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
        user.recipes.add(recipe)
        user.save()

        messages.success(request, "Recipe added successfully")

        return HttpResponseRedirect(reverse('recipes:list_recipe'))


def delete_recipe_from_account(request, pk):
    if request.POST:
        recipe = Recipe.objects.get(pk=pk)
        user = request.user
        user.recipes.remove(recipe)
        messages.success(request, "Recipe deleted successfully")

        return HttpResponseRedirect(reverse('recipes:user_recipes'))
