from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=300)
    portions = models.IntegerField(validators=[MinValueValidator(limit_value=1)])
    ingredients = models.CharField(max_length=300)
    steps = models.CharField(max_length=300)
    filters = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.title}"
