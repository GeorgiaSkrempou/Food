from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=300)
    portions = models.IntegerField(validators=[MinValueValidator(limit_value=1)])
    ingredients = models.CharField(max_length=300)
    steps = models.TextField()
    filters = models.CharField(max_length=300)

    user = models.ManyToManyField(User, related_name='recipes', blank=True)

    def __str__(self):
        return f"{self.title}"


