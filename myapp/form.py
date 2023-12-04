from myapp.models import Data
from django import forms

class RegisterForm(forms.ModelForm):
     class Meta:
          model = Data
          fields=['name','contact','address','mail']
          widgets={
               'name':forms.TextInput(attrs={'class':'form-control'}),
               'contact':forms.TextInput(attrs={'class':'form-control'}),
               'address':forms.TextInput(attrs={'class':'form-control'}),
               'mail':forms.TextInput(attrs={'class':'form-control'})
          }