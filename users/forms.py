from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Account,Devices

from django import forms
from django.forms import ModelForm


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Account
        fields = ('first_name','last_name','login','mobile_phone','address','email','feed_id','feed_id_access')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Account
        fields = ('login',)

class DevicesForm(forms.ModelForm):
    class Meta:
        model=Devices
        fields=('ESN',)