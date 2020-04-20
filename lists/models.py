from django.db import models


# Create your models here.
class List(models.Model):
    """list"""
    pass


class Item(models.Model):
    """Item"""
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)
