from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, nickname, company, name, password):
        user = self.model(
            nickname=nickname,
            name=name,
            company=company,
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, nickname, company, name, password):
        user = self.create_user(nickname=nickname,
                                company=company,
                                password=password,
                                name=name, )
        user.is_admin = True
        user.save(using=self.db)
        return user


class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    company = models.CharField(default='', max_length=100)
    name = models.CharField(default='', max_length=100)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'name'

    def __str__(self):
        return self.name
