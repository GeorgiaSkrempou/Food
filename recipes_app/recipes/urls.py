from django.urls import path

from .views import RecipeFormView, ThankYouView

app_name = 'recipes'

urlpatterns = [
    path("add_recipe/", RecipeFormView.as_view(), name='add_recipe'),
    path("thank_you/", ThankYouView.as_view(), name='thank_you')
]
