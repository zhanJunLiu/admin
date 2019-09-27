from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return JsonResponse({'status': 200, 'result': '注册'})

def logout(request):
    return JsonResponse({'status': 200, 'result': '退出登录'})

