from django import template
from main_app.models.products import Product as P
register = template.Library()

'''@register.filter(name='cart_product')
def cart_product(product  , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product:
            return P.objects.get(id=product).name
    return 0;
@register.filter(name='cart_product_code')
def cart_produc_code(product  , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product:
            return P.objects.get(id=product).product_code
    return 0;
@register.filter(name='cart_product_price')
def cart_produc_price(product  , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product:
            return P.objects.get(id=product).unit_price
    return 0;'''
    
@register.filter(name='is_in_cart')
def is_in_cart(product  , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False;


@register.filter(name='cart_quantity')
def cart_quantity(product  , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0;


@register.filter(name='price_total')
def price_total(product  , cart):
    return product.unit_price * int(cart_quantity(product , cart))


@register.filter(name='total_cart_price')
def total_cart_price(products , cart):
    sum = 0 ;
    for p in products:
        sum += price_total(p , cart)

    return sum
    