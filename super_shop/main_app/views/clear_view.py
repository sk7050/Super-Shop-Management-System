from django.shortcuts import render,redirect 
from django.views import View
class Clear_View(View):
    
    def get(self,request,id=None):
        if id:
            cart = request.session.get('cart')
            del cart[str(id)]
            request.session['cart']=cart
        else:
            request.session['cart']={}
        return redirect('order')
    def post(self,request,pk=None):
        
            pass
        
class Logout_View(View):
    
    def get(self,request,id=None):
        request.session['user']=None
        request.session['cart']={}
        return redirect('login')
    
        
        