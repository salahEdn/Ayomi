from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.http import HttpResponse
# Create your views here.  // delete comment
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User


def users_list(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'user_list.html', context)


def users_update(request, id):
    data = dict()
    user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        form.save()
        data['form_is_valid'] = True
        users = User.objects.all()
        data['user_list'] = render_to_string('user_list_2.html', {'users': users})
    else:
        form = UserForm(instance=user)

    context = {
        'form': form
    }
    data['html_form'] = render_to_string('user_update.html', context, request=request)
    return JsonResponse(data)


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Le compte a été créé pour ' + user)
            return redirect('/')
    context = {'form': form}
    return render(request, 'register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/users')
        else:
            messages.info(request, 'Utilisateur ou Mot de passe est incorrect')

    context = {}

    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('/')
