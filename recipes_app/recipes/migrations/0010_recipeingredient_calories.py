# Generated by Django 4.0.7 on 2023-03-19 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_alter_ingredient_options_alter_recipe_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipeingredient',
            name='calories',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
