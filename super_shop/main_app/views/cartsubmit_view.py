from django.shortcuts import render,redirect 
from django.http import HttpResponse
from main_app.models.products import Product
from main_app.models.customer import Customer
from main_app.models.orders import Order
from django.views import View

import json 


def Customer_Save(name,phone,email):
    Customer(customer_name=name,customer_phone=phone,customer_email=email).save()
    
def Order_Save(name,phone,email,products_dict,total_price):
    print(len(products_dict))
    if len(products_dict) > 2:
        obj=Order(customer_name=name,
                    customer_phone=phone,
                    customer_email=email,
                    products_dict=products_dict,
                    total_price=total_price,)
        obj.save()
        return obj
    
    return None
    
def Store_update_after_bill(cart):
    products = Product.get_products_by_id(list(cart.keys()))
    for product in products:
        qty=int(product.quantity)-int(cart[str(product.id)])    
        if qty <= 0:
                Product.objects.filter(id=product.id).update(quantity=0)
        else:
            Product.objects.filter(id=product.id).update(quantity=qty) 
def cart_product_list(cart):
    ids = list(cart.keys())            
    cart_products=Product.get_products_by_id(ids)
    return cart_products
def check_customer_list(phone,email) :
    obj=Customer.objects.filter(customer_phone=phone,customer_email=email)
    return len(obj)   
    
        
               
class Cartsubmit_View(View):
    context={}
    def get(self,request,id=None):
        pass
    
       
        
    def post(self,request,pk=None):
        try:
            name=request.POST['customer_name']
            phone=request.POST['customer_phone']
            email=request.POST['customer_email']
            if  check_customer_list(phone,email) <= 0:
                Customer_Save(name,phone,email)
            
        
            total_price=request.POST.get('total_price')
            total_price=float(total_price[2:])
            cart=request.session.get('cart')
            products_dict=json.dumps(cart)
            order_obj=Order_Save(name,phone,email,products_dict,total_price)
            if  order_obj is None:
                request.session['form_message']="Error"
                return redirect('order')
            Store_update_after_bill(cart)
            request.session['cart']={}
            return redirect ('pdf',id=order_obj.id)
            
        
        except:
            return HttpResponse(Exception)
            
        