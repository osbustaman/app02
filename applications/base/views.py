from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def controlPanel(request):
    lst_bases = []

    data = {
        'lst_bases': lst_bases,
    }
    return render(request, 'bases/listado_bases.html', data)