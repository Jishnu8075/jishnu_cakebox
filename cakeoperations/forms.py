from django import forms
from django.contrib.auth.forms import UserCreationForm
from cakeoperations.models import User,Category,Cakes,Offer,CakeVarients


class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2','phone','address']

class LoginForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput)

class CategoryCreateForm(forms.ModelForm):

    class Meta:
        model=Category
        fields=['caketype']

class CakeCreateForm(forms.ModelForm):
    class Meta:
        model=Cakes
        fields=('__all__')

class CakeVarientForm(forms.ModelForm):
    class Meta:
        model=CakeVarients
        fields="__all__"

class OfferCreateForm(forms.ModelForm):
    class Meta:
        model=Offer
        exclude=('cakevarient',)
        widgets={
        "start_date":forms.DateInput(attrs={"type":"date"}),
        "due_date":forms.DateInput(attrs={"type":"date"}),

        }