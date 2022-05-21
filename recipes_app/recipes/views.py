from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView
from django.urls import reverse_lazy


from .models import Recipe
# Create your views here.


class HomeView(TemplateView):
    template_name = 'recipes/home.html'


class ThankYouView(TemplateView):
    template_name = 'recipes/thank_you.html'


class RecipeCreateView(CreateView):
    # attribute names must be named like this
    model = Recipe
    # the form details are automatically saved like this
    fields = '__all__'
    #  success url? # it's the url not the template!
    success_url = reverse_lazy('recipes:thank_you')


# This lists every instance of the teacher
# model_list.hmtl
class RecipeListView(ListView):
    model = Recipe
    #  change the query done by django to something more custom
    queryset = Recipe.objects.order_by('title')
    #  replaces the object_list with recipe_list
    context_object_name = 'recipe_list'


class RecipeDetailView(DetailView):
    model = Recipe


class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = "__all__"
    success_url = reverse_lazy('recipes:detail_recipe')
