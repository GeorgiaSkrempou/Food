from django.urls import path

from .views import (RecipeCreateView, ThankYouView, RecipeListView, HomeView, RecipeDetailView, RecipeUpdateView,
                    RecipeDeleteView, SignUpView)

app_name = "recipes"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("add_recipe/", RecipeCreateView.as_view(), name="add_recipe"),
    path("thank_you/", ThankYouView.as_view(), name="thank_you"),
    path("list_recipe/", RecipeListView.as_view(), name="list_recipe"),
    path("detail_recipe/<int:pk>/", RecipeDetailView.as_view(), name="detail_recipe"),
    path("update_recipe/<int:pk>", RecipeUpdateView.as_view(), name="update_recipe"),
    path("delete_recipe/<int:pk>", RecipeDeleteView.as_view(), name="delete_recipe"),
    path("signup/", SignUpView.as_view(), name="signup")

]
