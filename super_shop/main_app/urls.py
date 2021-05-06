from django.urls import path
from main_app.views import user_view,dashboard
from django.contrib.auth import views as auth_views 
from .middlewares.auth import auth_middleware
from .views.user_view import Login_user
from .views.dashboard import Main_Panel
from main_app.forms.productforms import ProductForm
from main_app.forms.catagoriesform import  CategoryForm
from main_app.forms.customerform import CustomerForm
from .views.products_view import Product_Show
from .views.order_view import Creat_Order
from .views.add_cart import Add_Cart
from .views.clear_view import Clear_View,Logout_View
from .views.cartsubmit_view import  Cartsubmit_View
from .views.invoice_view import GeneratePdf
urlpatterns = [
    path('',Login_user.as_view(),name='login'),
    path('main/',auth_middleware(Main_Panel.as_view()),name='main'),
    path('main/product',Product_Show.as_view(tamplate_name='product.html',form_class=ProductForm),name='product'),
    path('main/order',Creat_Order.as_view(tamplate_name='order.html',form_class=CustomerForm),name='order'),
    path('main/order/add_cart',Add_Cart.as_view(),name='add_cart'),
    path('main/order/add_cart/cart_submit',Cartsubmit_View.as_view(),name='cart_submit'),
    path('main/order/clear/<id>',Clear_View.as_view(),name='clear'),
    path('main/order/clear/',Clear_View.as_view(),name='clear_all'),
    path('main/product/edit/<pk>',Product_Show.as_view(tamplate_name='product.html',form_class=ProductForm),name='edit'),
    path('main/product/delete/<pk>',Product_Show.as_view(tamplate_name='product.html',form_class=ProductForm),name='delete'),
    path('main/category',Product_Show.as_view(tamplate_name='product.html',form_class=CategoryForm),name='category'),
    path('signup/',user_view.signup_user, name='signup'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('main/order/invoce/<id>/', GeneratePdf.as_view(),name='pdf'),
    path('logout/',Logout_View.as_view(),name='logout'),
    ]