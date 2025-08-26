
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout      
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion')
    else:
        form = CustomUserCreationForm()
    return render(request, 'inscription.html', {'form': form})
    

def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            next_url = request.GET.get('next')  # récupère la page demandée
            if next_url:
                return redirect(next_url)
            return redirect('home')

        else:
            messages.error(request, 'Incorrect username or password.')
    return render(request, 'connexion.html')

@login_required
def home(request):
    return render(request, 'home.html')

def Logout(request):   
    logout(request) 
    return redirect('connexion')