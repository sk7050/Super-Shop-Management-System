# Super Shop Management System

This is web-based software which is developed by python with django .IT is so flexible easy to use.  This software can also use for Medicine Shop, Grocery Shop

## System Requirements for installation 
- have to install python 3.8.5
- have to install pip

## Installation Process
-  git clone this project to pc 
- run PowerShell as administrator
- then go to the project folder 

  For example:


             PS D:\> cd '.\Google Drive\Education\Paython\basic_supershop_management_system\

           

- then need to install pipenv
   

    For example:


            PS D:\Google Drive\Education\Paython\basic_supershop_management_system> pip install pipenv

            

       
                  
                   


- then need to install django using command pipenv install django


   For example:
             
        
       > pipenv install django


- activate vertual env by using pipenv shell command 

      
    For example:
             
        
       > pipenv shell

- then go to a folder where 'manage.py' in
   

    For example:
             
        
            > cd .\super_shop\
  
- then install requirements.txt by using command pip install -r requirements.txt


    For example:
             
        
            > pip install -r requirements.txt


- then run python manage.py runserver 


    For example:
             
        
            > python manage.py runserver
After running this window showing below message 

        System check identified no issues (0 silenced).
        May 05, 2021 - 20:54:46
        Django version 3.2, using settings 'super_shop.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK.


- open google chrome and go through http://127.0.0.1:8000/






## User Manual
By defult , here have a admin privilege

<img src="super_shop\static\img\login panel.PNG" width='300'>

*********************
email    =  admin@mail.com


password = 123


************************

Any of the employee who will use this software can sign up




<img src="super_shop\static\img\Signup.PNG" width='300'>




but can't acces to this without admin approval 

An admin can approve is_staff request by using admin panel





<img src="super_shop\static\img\panel.PNG" width='300'>

<img src="super_shop\static\img\permission.PNG" width='500'>



After admin approval , employee can login perfectly and do their job like add product,bill print,create order etc.




<img src="super_shop\static\img\admin panel.PNG" width='500'>

User can reset password.


