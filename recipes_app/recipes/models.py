from PIL import Image
from django.contrib.auth.models import User, AbstractBaseUser
from django.core.validators import MinValueValidator
from django.db import models
from ckeditor.fields import RichTextField

from user.models import Account


# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=300, blank=False)
    description = models.CharField(max_length=200, default="", blank=False)
    portions = models.IntegerField(validators=[MinValueValidator(limit_value=1)], blank=False)
    ingredients = RichTextField(blank=False)
    steps = RichTextField(blank=False)
    filters = models.CharField(max_length=300, blank=False)
    image = models.ImageField(default='recipe_default.jpg', upload_to='recipe_images', blank=True)

    user = models.ManyToManyField(Account, related_name='recipes', blank=True)

    def save(self, *args, **kwargs):
        super().save()

        if self.image:
            img = Image.open(self.image.path)

            # if img.height > 800 or img.width > 800:
            new_img = (450, 900)
            img.thumbnail(new_img)
            img.save(self.image.path)

    def __str__(self):
        return f"{self.title}"
