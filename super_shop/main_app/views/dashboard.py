from django.shortcuts import render,redirect 
from main_app.models.user_account import MyUser
from main_app.models.products import Product
from django.views import View


class Main_Panel(View):
    
    tamplate_name='main_panel.html'
    context={}
    def get(self,request):
        try:
            user=request.session.get('user')
            user_obj=MyUser.objects.get(phone=user)
        
            products=Product.get_all_products()
            self.context['user_obj']=user_obj
            self.context['products']=products
            return render(request,self.tamplate_name,self.context)
        except :
            return redirect('login')
        
    def post(self,request):
        return render(request,self.template_name)
    