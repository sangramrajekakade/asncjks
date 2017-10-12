from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, ListView
from .models import *
from django.views import generic
from django.shortcuts import render_to_response
from django.template import RequestContext



from creators.forms import *
# from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )

from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response


def login_view(request):
    print(request.user.is_authenticated())
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/complete")

        
    return render(request, "vifc/login.html", {"form":form})



def register_view(request):
    print(request.user.is_authenticated())
    form = UserRegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        print(request.user.is_authenticated())


    context = {
        "form":form

    }
    return render(request, "vifc/signup.html", context)

def logout_view(request):
    logout(request)
    return render(request, "vifc/index.html", {})

# Create your views here.
class HomePage(TemplateView):
    template_name = 'vifc/index.html'

# class Login(TemplateView):
#     template_name = 'vifc/login.html'

# class Signup(TemplateView):
#     template_name = 'vifc/signup.html'

class complete(TemplateView):
    template_name = 'vifc/complete.html'

