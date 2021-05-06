from django.db import models
from main_app.to_QR_CODE import make_qr
from django.core.files import File
from main_app.models.customer import Customer
import datetime


class Order(models.Model):
    
    customer_name=models.CharField(max_length=50)
    customer_phone=models.CharField(max_length=15)
    customer_email=models.CharField(max_length=15,blank=True)
    info_qr_code=models.ImageField(upload_to='uploads/qr_codes', blank=True)
    products_dict= models.TextField(max_length=10000) #list of product                            
    total_price = models.DecimalField(max_digits=15, decimal_places=2,default=0)
    date = models.DateField(default=datetime.datetime.today)
    
    def __str__(self):
        return self.customer_name
    
   
    def save(self, *args, **kwargs):
        
        content="Name:{customer_name} \n Phone:{customer_phone} \n email:{customer_email}".format(customer_name=self.customer_name,customer_phone=self.customer_phone,customer_email=self.customer_email)
        canvas,buffer,fname=make_qr(content=content)
        self.info_qr_code.save(fname,File(buffer),save=False)
        canvas.close()
        super().save(*args, **kwargs)

    
