from django.shortcuts import render,redirect 
from django.contrib import messages
from django.http import HttpResponse
from main_app.models.user_account import MyUser
from main_app.models.products import Product
from django.views import View



class Creat_Order(View):
    tamplate_name=''
    form_class=''
    context={}
    def get(self,request,pk=None):
        try:  
            cart = request.session.get('cart')
            if not  cart:
                    cart={}
                    request.session['cart']=cart
                    cart_products=0
            
            else:
                ids = list(request.session.get('cart').keys())
                cart_products = Product.get_products_by_id(ids)
            user=request.session.get('user')
            name=MyUser.objects.get(phone=user).name
        
            self.context['form']=self.form_class()
            self.context['name']=name
            self.context['products']=Product.get_all_products()
            self.context['cart_products']=cart_products
        
            message = None
            self.context['message']=message
            if request.session.get('form_message'):
                message=request.session['form_message']
                request.session['form_message'] =None  
                self.context['message']=message
           
            return render(request,self.tamplate_name,self.context)
        except:
            return redirect('login') 
    def post(self,request,pk=None):
        form=self.form_class(request.POST)
        if form.is_valid:
            form.save()
        return redirect('main')