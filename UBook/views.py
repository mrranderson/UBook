from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.core.mail import send_mail

from .models import (User, UBookProfile)

def index(request):
    return render(request, 'website/index.html', {})

def about(request):
    return render(request, 'website/about.html', {})

def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']

        new_user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)

        new_ubook = UBookProfile(user=new_user, address=address, city=city, state=state, zipcode=zipcode)

        new_ubook.save()

        send_mail('UBook Profile Created!', 'Dope af', 'ubookautoreply@gmail.com', [email], fail_silently=False)

        return HttpResponseRedirect(reverse('index'))



    if request.method == 'GET':
        return render(request, 'website/signUp.html', {})
