from django import forms

from application.models import User


class UserForm(forms.ModelForm):

    class Meta():
        model = User
        fields = ['nome', 'telefone', 'email'] 
