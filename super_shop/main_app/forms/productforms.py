from django import forms
from .fields import GroupedModelChoiceField
from main_app.models.category import Category
from main_app.models.products import Product
class ProductForm(forms.ModelForm):
    category = GroupedModelChoiceField(
        queryset=Category.objects.exclude(parent=None), 
        choices_groupby='parent')

    class Meta:
        model = Product
        fields = ('category','name', 'product_code', 'unit_price','quantity','description')
        
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['name'].label=''
            self.fields['name'].help_text=''
            self.fields['name'].widget.attrs.update({'class': "form-control",'placeholder':"Product Name"})
            self.fields['product_code'].label=''
            self.fields['product_code'].help_text=''
            self.fields['product_code'].widget.attrs.update({'class': "form-control",'placeholder':"Product Code"})
            self.fields['unit_price'].widget.attrs.update({'class':'form-control','placeholder':'Unit Price'})
            self.fields['unit_price'].label=''
            self.fields['unit_price'].help_text=''
            self.fields['quantity'].label=''
            self.fields['quantity'].help_text=''
            self.fields['quantity'].widget.attrs.update({'class': "form-control",'placeholder':"Quantity"})
            self.fields['description'].widget.attrs.update({'class':'form-control','placeholder':'Description'})
            self.fields['description'].label=''
            self.fields['description'].help_text=''
        
        
        
      