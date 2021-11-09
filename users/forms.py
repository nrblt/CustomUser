from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Account


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Account
        fields = ('first_name','last_name','login','mobile_phone','address','email','feed_id','feed_id_access')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Account
        fields = ('login',)
