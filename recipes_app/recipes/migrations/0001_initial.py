# Generated by Django 4.0.4 on 2022-06-02 09:36

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import recipes.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('profile_image', models.ImageField(blank=True, default=recipes.models.get_default_profile_image, max_length=255, null=True, upload_to=recipes.models.get_profile_image_filepath)),
                ('hide_email', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.CharField(default='', max_length=200)),
                ('portions', models.IntegerField(validators=[django.core.validators.MinValueValidator(limit_value=1)])),
                ('ingredients', models.CharField(max_length=300)),
                ('steps', models.TextField()),
                ('filters', models.CharField(max_length=300)),
                ('user', models.ManyToManyField(blank=True, related_name='recipes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
