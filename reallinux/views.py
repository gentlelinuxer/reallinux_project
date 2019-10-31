# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')

def real(request):
    return render(request, 'hello.html')

def send_json(request):
    data = [{'name': 'RealLinux', 'email': 'help@reallinux.co.kr'},
            {'name': 'Taeung Song', 'email': 'taeung@reallinux.co.kr'}]

    return JsonResponse(data, safe=False)
