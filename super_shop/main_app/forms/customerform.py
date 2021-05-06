from django import forms


from main_app.models.customer import Customer
class CustomerForm(forms.ModelForm):
    
    class Meta:
        model = Customer
        fields = ('customer_name', 'customer_phone', 'customer_email')
        
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['customer_name'].label=''
            self.fields['customer_name'].help_text=''
            self.fields['customer_name'].widget.attrs.update({'class': "form-control",'placeholder':"customer Name",'id':"name",'required':"True"})
            self.fields['customer_phone'].label=''
            self.fields['customer_phone'].help_text=''
            self.fields['customer_phone'].widget.attrs.update({'class': "form-control",'placeholder':"customer phone",'id':"phone",'required':"True"})
            self.fields['customer_email'].widget.attrs.update({'class':'form-control','placeholder':'customer_email','id':"email",'required':"True"})
            self.fields['customer_email'].label=''
            self.fields['customer_email'].help_text=''
            