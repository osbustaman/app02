from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('base_app:control-panel'))
        else:
            return render(request, 'base/login.html', {'error': 'Usuario o contraseña incorrectos.'})
    else:
        return render(request, 'base/login.html')
    
def logout_view(request):
    logout(request)
    response = redirect(reverse('account_base:accounts-login'))
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response
