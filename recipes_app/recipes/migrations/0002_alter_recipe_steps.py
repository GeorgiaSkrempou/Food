# Generated by Django 4.0.4 on 2022-05-21 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='steps',
            field=models.TextField(max_length=300),
        ),
    ]
