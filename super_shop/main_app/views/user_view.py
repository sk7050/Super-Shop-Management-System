from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password
from main_app.models.user_account import MyUser
from main_app.forms.userforms import UserCreationForm
from django.views import View
import re 



def email_check(mail):
      emaillist = list()
      detail=MyUser.objects.order_by("name")
      for i in detail:
        emaillist.append(str(i.email))

      if mail in emaillist:
           error="Already Exist this mail"
           return error
      else:
         error=0
         return error

def phone_check(phone):
      phonellist = list()
      detail=MyUser.objects.order_by("name")
      for i in detail:
        phonellist.append(str(i.phone))

      if phone in phonellist:
           error="Already Exist this phone number"
           return error
      else:
         error=0
         return error
def pass_check(psw1,psw2):
      if psw1 != psw2:
          error='Passwords are not same'
          return error
      elif len(psw1)<=6:
          error="Password's lenth should be grater then 6 digit"
          return error
      elif not re.search("[a-z]", psw1 ) or not re.search("[A-Z]", psw1 ) or not re.search("[0-9]", psw1 ) :
          error=''' The Password must be between [a-z]
                    At least one alphabet should be of Upper Case [A-Z]
                    At least 1 number or digit between [0-9].
                  '''
          return error
      else:
          error=0
          return error


        

def clean_password(password1,email):
        # Check that the two password entries match
        if email=='':
            error="Please  input your mail "
        elif password1=='':
            error="Please give your password "
        else:
            u = MyUser.objects.get(email=email)
            password2=u.password
            print(password2)
            if password1 and password2 and password1 != password2:
                error="password incorrect or email not found please try again"

        

        return error

# Create your views here.
class Login_user(View):
    return_url = None
    
    def get(self,request):
        if request.session.get('user'):
            return redirect('main')
            
        Login_user.return_url = request.GET.get('return_url')
        print(self.return_url)
        return render(request,'login.html')
    def post(self,request):
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, email=email, password=password)
        
        ''' checking is_staf or not if is is_staf then premit to login'''
        
        if user is not None:
            u=MyUser.objects.get(email=user) #here u is the instance of MyUser
            
            if u.is_staf:
                request.session['user']=u.phone
                print(self.return_url)
                
                if Login_user.return_url:
                    return HttpResponseRedirect(Login_user.return_url)
                else:
                    Login_user.return_url = None
                    login(request, user)
                    return redirect('main')
            else:
                messages.warning(request,"Still pending for staff request please call to admin")
                return render(request,'login.html')
        else:
            error=clean_password(request.POST['password'],request.POST['email'])
            print(error)
            messages.error(request,error)
            return render(request,'login.html')

        
            


def signup_user(request):
    
    form=UserCreationForm
    
    context={'form':form}
    if  request.method == "POST":
        email = request.POST['email']
        phone=  request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        error=pass_check(password1,password2)
        print(error)
        messages.error(request,error)
        if error == 0:
            data=form(request.POST)
            try:
                if data.is_valid:
                    data.save()
                    return redirect('login')
            except:
                error=email_check(email) or phone_check(phone)
                messages.error(request,error)
    
    return render(request,'signup.html',context)
    
