import random

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import *
class LoginUser(LoginView):
    form_class = UserLogin
    success_url = reverse_lazy('menu')
    template_name = 'registration/login.html'

class RegisterUser(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
    extra_context = {'title': 'Registration'}

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profil.html', context)


def SendEmail(request):
    form = EmailForm()
    if request.method == "POST":
        uname = request.POST['uname']
        email = request.POST['email']
        a=random.random()
        num=str(a)
        token=num.split('.')[1]
        user=EmailForm(uname=uname,email=email,token=token)
        user.save()
        domain_name=get_current_site(request).domain
        link=f"http://{domain_name}/verify/{uname}/{token}"
        send_mail('Email tasdiqlandi', f"Email manzilni tasdiqlash uchun {link} havolaga bosing...",
        settings.EMAIL_HOST_USER
        [email],
                  fail_silently=False)
        return HttpResponse('tasdiqlash yuborildi')
    return render(request,'profil.html',{'form':form})


# def ko'rinish
# def user_login(request):
#     if request.user.is_authenticated:
#         return redirect('menu')
#
#     if request.method == 'POST':
#         userlogin = request.POST['user_login']
#         password = request.POST['password']
#
#         user = authenticate(request, username=userlogin, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('menu')
#         else:
#             print('error')
#     return render(request, 'registration/login.html')

# def user_logout(request):
#     logout(request)
#     return redirect('register')


# def register(request):
#     if request.method == 'POST':
#         form = UserRegister(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             return render(request, 'registration/register.html', {'form': form})
#
#         else:
#             print('error')
#             form = UserRegister()
#         return render(request, 'registration/register.html', {'form': form})
