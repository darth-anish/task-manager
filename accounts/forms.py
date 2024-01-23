from django import forms
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    username = forms.fields.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'autofocus': 'autofocus', 'class': 'form-control mb-3'}), label=False)
    password = forms.fields.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}), label=False)