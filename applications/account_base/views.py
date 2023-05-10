from django.shortcuts import render

from django.contrib.auth import authenticate, login
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
            return HttpResponseRedirect(reverse('controlPanel'))
        else:
            return render(request, 'base/login.html', {'error': 'Usuario o contraseña incorrectos.'})
    else:
        return render(request, 'base/login.html')
