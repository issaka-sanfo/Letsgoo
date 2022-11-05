from django.shortcuts import render, redirect
from django.contrib import messages
import os

def home(request):
    if request.user.is_authenticated:
        messages.success(request, 'Welcome back dear member!')
        return render(request,'live_home.html')
    messages.success(request, 'Welcome dear, feel free to register whenever you want! Bienvenu(e), vous pouvez créer un compte quand vous voulez!')
    return render(request,'live_home.html')


def signup(request):
    if request.method == 'POST':
        #first_name = request.POST['fname']
        last_name = request.POST['lname']
        mail = request.POST['emailOrPhone']
        pwd = request.POST['pwd']

        if User.objects.filter(username=mail):
            messages.warning(request, 'User name exist, change username!')
            messages.warning(request, 'Le nom d\'utilisateur existe, changez de nom d\'utilisateur !')
        else:
            new_user = User.objects.create_user(mail, mail, pwd)
            #new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.save()
            messages.success(request, 'Account has been created successfully.')
    return redirect('live_chat')


def user_login(request):
    if not request.user.is_authenticated:

        if request.method == 'POST':
            uname = request.POST['emailOrPhone2']
            pwd = request.POST['pwd']

            check_user = authenticate(username = uname.lower(), password = pwd)
            if check_user is not None:
                login(request, check_user)
                return redirect('')
            else:
                messages.warning(request, 'Invalid Username or Password.')
                return redirect('live_chat')
        return redirect('')

