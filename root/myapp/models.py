from typing import ClassVar
from django.db import models


# Create your models here.

class USER(models.Model):
    firstname:models.CharField(max_length=100)
    lastname: models.CharField(max_length=100)
    username:models.CharField(max_length=40)
    email:models.CharField(max_length=100)
    password:models.CharField(max_length=100)


class accountholder(models.Model):
    first_name:models.CharField(max_length=100)
    lastname: models.CharField(max_length=100)
    username:models.CharField(max_length=40)
    email:models.CharField(max_length=100)
    password:models.CharField(max_length=100)
    etst: models.CharField(max_length=1)