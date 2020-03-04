from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import get_user_model
from users.forms import SignUpForm, LoginForm
from users.models import Logs


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'users/signup.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        user = request.user.username
        adr = request.META.get('REMOTE_USER_ADDR')
        agent = request.META.get('HTTP_USER_AGENT ')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        # User system details
        obj = Logs.objects.using('logs').create(user=user, ipaddr=adr, user_agent=agent)
        obj.save(using='logs')
        #end
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect(reverse('drive'))

    context = {'form': form}
    return render(request, 'users/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')