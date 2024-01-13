from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm


class UserLogin(AuthenticationForm):
    username = forms.CharField(label='Log In',widget=forms.TextInput(attrs={'class' : 'form-input'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-input'}))
    class Meta:
        model = get_user_model()
        fields = ['username','password']




   
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
              raise forms.ValidationError('Sizning Emailingiz mavjud')
        return email

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=250)
    last_name = forms.CharField(max_length=250)

    class Meta:
        model = User
        fields = ['username', 'email','last_name','first_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class EmailForm(forms.ModelForm):
    uname = models.CharField(max_length=250)
    emial = models.EmailField()

# class UserRegister(UserCreationForm):
#     username = forms.CharField(label='Log In', widget=forms.TextInput(attrs={'class': 'form-input'}))
#     email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
#     password2 = forms.CharField(label='Password Again', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

#     class Meta:
#         model = get_user_model()
#         fields = ['username','email', 'password1','password2']