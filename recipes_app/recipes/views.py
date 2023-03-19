import random
from datetime import datetime

import pytz
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from .forms import RecipeForm, IngredientFormSet
from .models import Recipe, Ingredient
from .utils import add_ingredient_quantities


# Create your views here.


class HomeView(ListView):
    template_name = 'recipes/home.html'
    model = Recipe
    context_object_name = 'recipe_list'
    queryset = Recipe.objects.order_by('title')


@login_required
def shopping_list(request):
    return render(request, template_name='404.html')


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm

    success_url = reverse_lazy('recipes:list_recipe')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['recipe_ingredient'] = IngredientFormSet(self.request.POST)
        else:
            data['recipe_ingredient'] = IngredientFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        ingredient = context['recipe_ingredient']
        self.object = form.save()
        if ingredient.is_valid():
            ingredient.instance = self.object
            ingredient.save()
        else:
            messages.error(self.request, "Please fill in the ingredients form correctly")
            return self.render_to_response(self.get_context_data(form=form))
        return super().form_valid(form)


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['recipe_ingredient'] = IngredientFormSet(self.request.POST, instance=self.object)
        else:
            data['recipe_ingredient'] = IngredientFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        ingredient = context['recipe_ingredient']
        self.object = form.save()

        if ingredient.is_valid():
            ingredient.instance = self.object
            ingredient.save()
        else:
            messages.error(self.request, "Please fill in the ingredients form correctly")
            return self.render_to_response(self.get_context_data(form=form))
        
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("recipes:detail_recipe", kwargs={"pk": pk})


@login_required
def recipe_list(request):
    recipes = Recipe.objects.order_by('title')
    user = request.user
    paginator = Paginator(recipes, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    if request.POST.get('shop'):
        selected_recipes = request.POST.getlist('recipe-checkbox')

        if selected_recipes:
            unique_ingredient_list = add_ingredient_quantities(selected_recipes=selected_recipes)
            return render(request, 'recipes/shopping_list.html', {'ingredient_list': unique_ingredient_list})
        else:
            messages.warning(request, "Please select a recipe first")
            return HttpResponseRedirect(reverse('recipes:list_recipe'))

    elif request.POST.get('add-to-my-recipes'):
        selected_recipes = request.POST.getlist('recipe-checkbox')

        if selected_recipes:
            for recipe_id in selected_recipes:
                recipe = Recipe.objects.get(pk=recipe_id)
                user_recipes = Recipe.objects.filter(user=user).order_by('title')
                if recipe not in user_recipes:
                    recipe.user.add(user)
                    messages.success(request, f"{recipe.title} was successfully added to your account")
                else:
                    messages.warning(request, f"{recipe.title} is already in your account")
        else:
            messages.warning(request, "Please select a recipe first")

    elif request.POST.get('delete'):
        selected_recipes = request.POST.getlist('recipe-checkbox')
        if selected_recipes:
            for recipe_id in selected_recipes:
                recipe = Recipe.objects.get(pk=recipe_id)
                recipe.delete()
                messages.success(request, f"{recipe.title} was deleted successfully")
        else:
            messages.warning(request, "Please select a recipe first")

        return HttpResponseRedirect(reverse('recipes:list_recipe'))

    context = {
        'recipes_list': recipes,
        'page_obj': page_obj,
        'load_more_url': 'recipes:list_recipe',
        'show_edit_btn': True,
    }

    if request.htmx:
        return render(request, template_name='recipes/recipes_table.html', context=context)
    return render(request, template_name='recipes/recipe_list.html', context=context)


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe


@login_required
def user_recipes_list(request):
    user = request.user
    user_recipes = Recipe.objects.filter(user=user).order_by('title')
    paginator = Paginator(user_recipes, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    def get_random_recipe():

        current_date = datetime.now(pytz.timezone('Europe/Amsterdam'))
        # tomorrow = current_date + timedelta(days=5)
        num_date_time = int(current_date.strftime('%d%m%Y'))
        recipes_list = Recipe.objects.filter(user=user).all()
        random.seed(num_date_time)
        if not recipes_list:
            return None

        random_recipe = random.choice(recipes_list)

        return random_recipe

    if request.POST.get('shop'):
        selected_recipes = request.POST.getlist('recipe-checkbox')

        if selected_recipes:
            unique_ingredient_list = add_ingredient_quantities(selected_recipes=selected_recipes)
            return render(request, 'recipes/shopping_list.html', {'ingredient_list': unique_ingredient_list})
        else:
            messages.warning(request, "Please select a recipe first")
            return HttpResponseRedirect(reverse('recipes:user_recipes'))

    elif request.POST.get('delete'):
        selected_recipes = request.POST.getlist('recipe-checkbox')
        # user = request.user
        if selected_recipes:
            for recipe_id in selected_recipes:
                recipe = Recipe.objects.get(pk=recipe_id)
                recipe.user.remove(user)
                messages.success(request, f"{recipe.title} was deleted successfully")
        else:
            messages.warning(request, "Please select a recipe first")

        return HttpResponseRedirect(reverse('recipes:user_recipes'))

    random_recipe = get_random_recipe()
    context = {'recipes_list': user_recipes,
               'random_recipe': random_recipe,
               'page_obj': page_obj,
               'load_more_url': 'recipes:user_recipes',
               'show_edit_btn': False}

    if request.htmx:
        return render(request, template_name='recipes/recipes_table.html', context=context)
    return render(request, template_name='recipes/user_recipes.html', context=context)


@login_required
def ingredient_list_view(request):
    ingredient_list = Ingredient.objects.order_by('name')
    # paginator = Paginator(ingredient_list, 10)
    # page_number = request.GET.get('page', 1)
    # page_obj = paginator.get_page(page_number)

    if request.POST.get('delete'):
        selected_ingredients = request.POST.getlist('recipe-checkbox')
        if selected_ingredients:
            for ingredient_id in selected_ingredients:
                ingredient = Ingredient.objects.get(pk=ingredient_id)
                ingredient.delete()
                messages.success(request, f"{ingredient.name} was deleted successfully")
        else:
            messages.warning(request, "Please select an ingredient first")

        return HttpResponseRedirect(reverse('recipes:list_ingredient'))

    context = {'ingredient_list': ingredient_list}
    # 'page_obj': page_obj,
    # 'load_more_url': 'recipes:list_ingredient'}

    # if request.htmx:
    #     return render(request, template_name='recipes/ingredients_table.html', context=context)
    return render(request, template_name='recipes/ingredient_list.html', context=context)


class IngredientCreateView(LoginRequiredMixin, CreateView):
    model = Ingredient
    fields = '__all__'
    success_url = reverse_lazy('recipes:list_ingredient')


class IngredientUpdateView(LoginRequiredMixin, UpdateView):
    model = Ingredient
    fields = '__all__'
    success_url = reverse_lazy('recipes:list_ingredient')
