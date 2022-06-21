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
    quantity = models.FloatField(blank=False)
    unit = models.CharField(max_length=30, blank=False)
    contains = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return f"{self.name}"


class Recipe(models.Model):
    title = models.CharField(max_length=300, blank=False)
    description = models.CharField(max_length=200, default="", blank=False)
    portions = models.IntegerField(validators=[MinValueValidator(limit_value=1)], blank=False)
    ingredients = RichTextField(blank=False)
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
    recipe_ingredients = models.ManyToManyField(Ingredient, related_name='ingredient', blank=False)

    def __str__(self):
        return f"{self.title}"
