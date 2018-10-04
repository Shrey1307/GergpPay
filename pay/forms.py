from . models import *
from django import forms
from django.forms import ModelForm

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Form 
        fields = '__all__'


class CouponForm(forms.ModelForm):
    class Meta:
        model = Coupons
        fields = '__all__'
