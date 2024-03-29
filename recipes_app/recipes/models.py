from ckeditor.fields import RichTextField
from django.contrib.auth.models import User, AbstractBaseUser
from django.core.validators import MinValueValidator
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from user.models import Account


# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=300, blank=False)
    contains = models.CharField(max_length=300, blank=True)

    class Meta:
        verbose_name = 'Ingredient'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=300, blank=False)
    description = models.CharField(max_length=200, default="", blank=False)
    portions = models.IntegerField(validators=[MinValueValidator(limit_value=1)], blank=False)
    steps = RichTextField(blank=False)
    filters = models.CharField(max_length=300, blank=False)
    image = models.ImageField(default='recipe_default.jpg', upload_to='recipe_images', blank=True, null=True)
    resized_image_large = ImageSpecField(
        source='image',
        processors=[ResizeToFill(600, 230)],
        format='PNG',
        options={'quality': 100},
    )

    user = models.ManyToManyField(Account, related_name='recipes', blank=True)
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name='ingredient',
        blank=False,
        through='RecipeIngredient'
    )
    total_calories = models.IntegerField(null=True, blank=True)

    def save(self):
        super().save()
        total_cal = 0
        for ingredient in self.ingredients.all():
            recipe_ingredient = RecipeIngredient.objects.get(recipe=self, ingredient=ingredient)
            if recipe_ingredient.calories:
                total_cal += recipe_ingredient.calories
        self.total_calories = total_cal
        return super().save()

    class Meta:
        verbose_name = 'Recipe'

    def __str__(self):
        return self.title


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(blank=False, null=True)
    unit = models.CharField(max_length=30, blank=False, null=True)
    calories = models.IntegerField(null=True, blank=False)

    class Meta:
        verbose_name = 'Recipe_ingredient'
        unique_together = ('recipe', 'ingredient')


    def __str__(self):
        return f"{self.recipe.title} - {self.ingredient.name}"
