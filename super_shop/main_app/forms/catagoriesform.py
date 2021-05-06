from django import forms
from main_app.models.category import Category
class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = '__all__'