from .models import RecipeIngredient


def add_ingredient_quantities(selected_recipes):
    ingredient_list = RecipeIngredient.objects.filter(recipe_id__in=selected_recipes)
    unique_ingredient_list = {}
    for ingredient_object in ingredient_list:
        ingredient_id = ingredient_object.ingredient_id
        if ingredient_object.ingredient_id not in unique_ingredient_list:
            unique_ingredient_list[ingredient_id] = {
                'ingredient': ingredient_object.ingredient,
                'quantity': 0,
                'unit': '',
            }
        unique_ingredient_list[ingredient_id]['quantity'] += ingredient_object.quantity
        unique_ingredient_list[ingredient_id]['unit'] = ingredient_object.unit
    return unique_ingredient_list
