from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    name = models.CharField(verbose_name='名前', max_length=30)
    gender = models.CharField(verbose_name='性別', max_length=30)
    age = models.CharField(verbose_name='年齢', max_length=30)

class Number(models.Model):
    num = models.IntegerField()