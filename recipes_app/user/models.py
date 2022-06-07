from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models
from PIL import Image


# Create your models here.


class MyAccountManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError
        if not username:
            raise ValueError
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    avatar = models.ImageField(default='default.png', upload_to='profile_images')

    def save_image(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 500 or img.width > 500:
            new_img = (500, 500)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

    objects = MyAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


# class Avatar(models.Model):
#     user = models.OneToOneField(Account, on_delete=models.CASCADE)
#
#     avatar = models.ImageField(default='default.png', upload_to='profile_images')
#
#     def save(self, *args, **kwargs):
#         super().save()
#
#         img = Image.open(self.avatar.path)
#
#         if img.height > 500 or img.width > 500:
#             new_img = (500, 500)
#             img.thumbnail(new_img)
#             img.save(self.avatar.path)
#
#     def __str__(self):
#         return self.user.username
