from django.http import HttpResponse
from django.views.generic import View
from main_app.models.customer import Customer
from main_app.to_pdf import  render_to_pdf 
from main_app.models.orders import Order
from main_app.models.products import Product
import json
from num2words import num2words


class GeneratePdf(View):
    context={}
    def get(self,request,id):
        try:
            cart=json.loads(Order.objects.get(id=id).products_dict)
            self.context['cart']=cart
            order=Order.objects.get(id=id)
            total_price=order.total_price
            self.context['total_price']=num2words(total_price)
            self.context['order']=order
            self.context['products']=Product.get_products_by_id(ids=list(cart.keys()))
            pdf = render_to_pdf('invoice.html', self.context)
            response=HttpResponse(pdf, content_type="application/pdf")
            response['Content-Disposition'] = f'filename=order_{id}.pdf'
            return response
        except:
            return HttpResponse("<h1>Please input valid bill no</h1>")
             

        
