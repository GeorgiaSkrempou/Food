from django.contrib import admin

from .models import Recipe, RecipeInstance

# Register your models here.


admin.site.register(Recipe)
admin.site.register(RecipeInstance)

