# Generated by Django 4.0.4 on 2022-06-07 14:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('user', '0003_alter_account_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='avatar',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='profile_images'),
        ),
    ]
