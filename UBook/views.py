from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout

from .models import (User, UBookProfile)

import stripe

def index(request):
    return render(request, 'website/index.html', {})

def about(request):
    return render(request, 'website/about.html', {})

def auth_login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        login(request, user)

        return HttpResponseRedirect(reverse('index'))

    else:
        return HttpResponseRedirect(reverse('index'))


def auth_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

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

        new_user = authenticate(username=username, password=password)
        login(request, new_user)

        return HttpResponseRedirect(reverse('index'))

    if request.method == 'GET':
        return render(request, 'website/signUp.html', {})

def charge(request):

    if request.method == 'POST':
        # Set your secret key: remember to change this to your live secret key in production
        # See your keys here https://dashboard.stripe.com/account/apikeys
        stripe.api_key = "sk_test_EqcgbisfuVnctYONDROGsHYd"

        # Get the credit card details submitted by the form
        token = request.POST['stripeToken']

        # Create the charge on Stripe's servers - this will charge the user's card
        try:
          charge = stripe.Charge.create(
              amount=1000, # amount in cents, again
              currency="usd",
              source=token,
              description="Example charge"
          )
        except stripe.error.CardError as e:
          # The card has been declined
          pass
        return HttpResponseRedirect(reverse('index'))

    return render(request, 'website/charge.html', {})