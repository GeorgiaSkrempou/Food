# Generated by Django 4.0.4 on 2022-06-06 15:40

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_alter_recipe_steps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
