from django.db import  models


class Customer(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_phone = models.CharField(max_length=15)
    customer_email = models.EmailField()
    

    def __str__(self):
        return self.customer_name
    def register(self):
        self.save()