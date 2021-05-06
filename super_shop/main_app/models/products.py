from django.db import models
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=50)
    product_code=models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    unit_price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=200, default='' , null=True , blank=True)
    quantity=models.CharField(max_length=50,blank=True) #--------------------------------->current stock in  in units
    image = models.ImageField(upload_to='uploads/products/',blank=True)
    
    def __str__(self):
        return self.name
    
    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in =ids)


    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products();