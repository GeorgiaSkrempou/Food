# Generated by Django 4.0.4 on 2022-05-27 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_alter_recipe_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RecipeInstance',
        ),
    ]