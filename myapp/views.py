from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os
from myproject.settings import BASE_DIR

def login_page(request):
    print(os.path.join(BASE_DIR, 'static'))
    return render(request, 'login.html')


def show_sign_up(request):
    print(os.path.join(BASE_DIR, 'static'))
    return render(request, 'sign.html')

def store_page(request):
    print(os.path.join(BASE_DIR, 'static'))
    return render(request, 'firstpage.html')
