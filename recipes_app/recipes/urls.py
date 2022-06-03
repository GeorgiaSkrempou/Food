from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import (RecipeCreateView, RecipeListView, HomeView, RecipeDetailView, RecipeUpdateView,
                    RecipeDeleteView, UserRecipesView, add_recipe_to_account, delete_recipe_from_account,
                    random_recipe_view)

app_name = "recipes"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("add_recipe/", RecipeCreateView.as_view(), name="add_recipe"),
    path("list_recipe/", RecipeListView.as_view(), name="list_recipe"),
    path("detail_recipe/<int:pk>/", RecipeDetailView.as_view(), name="detail_recipe"),
    path("update_recipe/<int:pk>", RecipeUpdateView.as_view(), name="update_recipe"),
    path("delete_recipe/<int:pk>", RecipeDeleteView.as_view(), name="delete_recipe"),
    path("user_recipes/", UserRecipesView.as_view(), name='user_recipes'),
    path("add_recipe_to_account/<int:pk>", add_recipe_to_account, name="add_recipe_to_account"),
    path("delete_recipe_from_account/<int:pk>", delete_recipe_from_account, name="delete_recipe_from_account"),
    path("random_recipe/", random_recipe_view, name="random_recipe")
]
