from django.db import  models
from unittest.util import _MAX_LENGTH

class Category(models.Model):
    name = models.CharField(max_length=20)
    parent = models.CharField(max_length=20,null=True)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()


    def __str__(self):
        return self.name