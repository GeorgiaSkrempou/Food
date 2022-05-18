from django.urls import path

from .views import RecipeCreateView, ThankYouView, RecipeListView, HomeView

app_name = 'recipes'

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("add_recipe/", RecipeCreateView.as_view(), name='add_recipe'),
    path("thank_you/", ThankYouView.as_view(), name='thank_you'),
    path("list_recipe/", RecipeListView.as_view(), name="list_recipe")
]
