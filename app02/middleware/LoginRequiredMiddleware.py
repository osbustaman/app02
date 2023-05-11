from django.shortcuts import redirect
from django.urls import reverse

from django.shortcuts import render

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        if not request.user.is_authenticated:
            response = redirect(reverse('account_base:accounts-login'))
            return response

        response = self.get_response(request)
        return response
