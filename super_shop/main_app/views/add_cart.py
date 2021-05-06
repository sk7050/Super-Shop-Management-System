from django.shortcuts import render,redirect 
from django.contrib import messages
from django.http import HttpResponse
from main_app.models.products import Product
from django.views import View


class Add_Cart(View):

    def post(self , request):
        product = request.POST['product']
        print(product)
        qty = request.POST.get('qty')
        if  int(qty) > int(Product.objects.get(id=int(product)).quantity):
            request.session['form_message']="The number of Quantity"+qty+" is not in stok"
            return redirect('order')
        
        
      
        cart = request.session.get('cart')
        if cart:
            if product in list(cart.keys()):
                cart[product]=int(qty)+int(cart[product])
            else:
                cart[product]=qty
        else:
            cart = {}
            cart[product] = qty

        request.session['cart'] = cart     
        return redirect('order')
        