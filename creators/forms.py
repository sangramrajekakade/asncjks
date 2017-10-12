#files.py
# import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )


#User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate (username=username, password=password)
        # user_qs = User.objects.filter(username=username)
        # if user_qs.count() == 1:
        #     user = user_qs.first()
        if not user:
            raise forms.ValidationError("This User Does Not Exist")

        if not user.check_password(password):
            raise forms.ValidationError("Incorect Password")


        if not user.is_active:
            raise forms.ValidationError("This User Not Longer Active")
        return super(UserLoginForm, self).clean(*args, **kwargs)
 
class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email Adress')
    email_confirm = forms.EmailField(label='Confirm Email')
    password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email_confirm',           
            'password'

        ]
    def clean_email_confirm(self):
        email = self.cleaned_data.get('email')
        email_confirm = self.cleaned_data.get('email_confirm')


        if email != email_confirm:
            raise forms.ValidationError("Email Must Match")

            email_qs = User.objects.filter(email=email)
            if email_qs.exists():
                raise form.ValidationError("This Email has already been Register")

            return email