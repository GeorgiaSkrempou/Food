# Generated by Django 4.0.4 on 2022-06-05 21:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='recipe_default.png', upload_to='recipe_images'),
        ),
    ]
