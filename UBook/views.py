from django.http import response
from django.shortcuts import render

def index(request):
    return render(request, 'website/index.html', {})

def about(request):
    return render(request, 'website/about.html', {})

def signup(request):

    if request.method == 'GET':
        return render(request, 'website/signUp.html', {})

