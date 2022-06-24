from django.urls import path

from .views import (RecipeCreateView, RecipeListView, HomeView, RecipeDetailView, RecipeUpdateView,
                    RecipeDeleteView, UserRecipesView,
                    IngredientCreateView, IngredientListView, IngredientUpdateView, IngredientDeleteView, shopping_list)

app_name = "recipes"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("add_recipe/", RecipeCreateView.as_view(), name="add_recipe"),
    path("list_recipe/", RecipeListView.as_view(), name="list_recipe"),
    path("detail_recipe/<int:pk>/", RecipeDetailView.as_view(), name="detail_recipe"),
    path("update_recipe/<int:pk>/", RecipeUpdateView.as_view(), name="update_recipe"),
    path("delete_recipe/<int:pk>/", RecipeDeleteView.as_view(), name="delete_recipe"),
    path("user_recipes/", UserRecipesView.as_view(), name='user_recipes'),
    path("add_ingredient/", IngredientCreateView.as_view(), name="add_ingredient"),
    path("list_ingredient/", IngredientListView.as_view(), name="list_ingredient"),
    path("update_ingredient/<int:pk>/", IngredientUpdateView.as_view(), name="update_ingredient"),
    path("delete_ingredient/<int:pk>/", IngredientDeleteView.as_view(), name="delete_ingredient"),
    path("shopping_list/", shopping_list, name="shopping_list"),
]
