from django.contrib import admin
from django import forms

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from .models.customer import Customer
from .models.products import Product
from .models.category import Category
from .models.orders import Order
from .models.user_account import MyUser

''' 
-----------------------------------------------------------------------------------------------------------
start admin panel for user 
'''
class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email', 'name','phone')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'name','phone', 'is_active', 'is_admin','is_staf')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email','name','phone', 'is_admin','is_staf')
    list_filter = ('is_admin','is_staf')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name','phone')}),
        ('Permissions', {'fields': ('is_admin','is_staf')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name','phone', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()
    
    # Now register the new UserAdmin...
admin.site.register(MyUser, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)

'''
-------------------------------------------------------------------------------------------------------
end user admin panel
'''

""" 
------------------------------------------------------------------------------------------------------
Start Products related admin panel 
"""
@admin.register(Product)
class Product_show(admin.ModelAdmin):
    list_display=("name","product_code","category","quantity","unit_price")
@admin.register(Category)
class Category_show(admin.ModelAdmin):
    pass
@admin.register(Customer)
class Customer_show(admin.ModelAdmin):
    pass


@admin.register(Order)
class Orde_show(admin.ModelAdmin):
    list_display=("date","customer_name","customer_phone","product_info","Total_price")

    def Total_price(self,obj):
        return str(obj.total_price)+" "+"Tk"
    def product_info(self,obj):
        product_list=[] # empty list
        dictionary ={} #empty dict
        cart=(obj.products_dict)# cart is the jeson string but next to process string to dict
        cart_str = cart.replace("{" ,"").replace("}" , "") #--------- Third bracket replace by empty string
        
        cart_list = cart_str.split(",") #-----products separated by comma(,) and this is a list 
       
        #print(list)
        for i in cart_list:
            if len(i) > 3:
                key,value=i.strip().split(":")
                keys=key.replace('"','')
                
                dictionary[keys]=value

                product=Product.objects.get(id=int(keys)).name
                qtn=value
                product_details="Product Names :{product} \n Quantity:{quantity} \n".format(product=product,quantity=qtn)
                
                product_list.append(product_details)

           
           
            
        print(dictionary)    
        return product_list


        """
        ------------------------------------------------------------------------------------------------------
        End Product related admin panel
        """