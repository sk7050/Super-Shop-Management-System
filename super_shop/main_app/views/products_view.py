from django.shortcuts import render,redirect 
from django.http import HttpResponse
from main_app.models.user_account import MyUser
from main_app.models.products import Product
from django.views import View



class Product_Show(View):
    tamplate_name=''
    form_class=''
    context={}
    def get(self,request,pk=None):
        try:
            user=request.session.get('user')
            name=MyUser.objects.get(phone=user).name
            form=self.form_class
        
            if pk:
                if 'delete' in request.path:
                    Product.objects.get(pk=pk).delete()
                    return redirect('main')
                
                obj=Product.objects.get(pk=pk)
                form=self.form_class(instance=obj)
            self.context['form']=form
            self.context['name']=name
            return render(request,self.tamplate_name,self.context)
        except :
            return redirect('login')
    def post(self,request,pk=None):
        form=self.form_class(request.POST)
        if pk:
            obj=Product.objects.get(pk=pk)
            form=self.form_class(request.POST,instance=obj)
        if form.is_valid:
            print('valid')
            form.save()
             
        return redirect('main')
    
    

        