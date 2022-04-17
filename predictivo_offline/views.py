from pickle import FALSE
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MedicionForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def loginPage(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Usuario inexistente')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Password inválido')

    context = {'page': page}
    return render(request, 'login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    page = 'register'

    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'Ocurrió un error durante el registro')    

    context = {'page': page, 'form': form}
    return render(request, 'login_register.html', context)

def home(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def mediciones(request):
    form = MedicionForm()

    if request.method == 'POST':
        form = MedicionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form' : form}
    return render(request, 'registrar_med.html', context)