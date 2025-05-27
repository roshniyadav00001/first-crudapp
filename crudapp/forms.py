
from .models import customer
from django import forms  

class customerform(forms.ModelForm):
    
    class Meta:
        model = customer
        fields = '__all__'

