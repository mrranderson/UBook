from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse

from .models import User
from UBook.models import UBookProfile, UBookProfileForm

import stripe


def index(request, **kwargs):
    return render(request, 'website/index.html', {'kwargs': kwargs})


def about(request):
    return render(request, 'website/about.html', {})


def auth_login(request):
    if request.method == 'POST':
        try:
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request, user)
        except:
            pass

        return HttpResponseRedirect(reverse('index'))

    else:
        return HttpResponseRedirect(reverse('index'))


def auth_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def signup(request):
    if request.method == 'POST':

        signup_form = UBookProfileForm(request.POST)

        if signup_form.is_valid():
            new_user = User.objects.create_user(username=signup_form.cleaned_data['username'],
                                                password=signup_form.cleaned_data['password'],
                                                email=signup_form.cleaned_data['email'],
                                                first_name=signup_form.cleaned_data['first_name'],
                                                last_name=signup_form.cleaned_data['last_name'])

            new_user.save()

            new_ubook = UBookProfile(user=new_user,
                                     address=signup_form.cleaned_data['address'],
                                     city=signup_form.cleaned_data['city'],
                                     state=signup_form.cleaned_data['state'],
                                     zipcode=signup_form.cleaned_data['zipcode'],
                                     cc_type=signup_form.cleaned_data['cc_type'],
                                     cc_number=signup_form.cleaned_data['cc_number'],
                                     cc_expdate=signup_form.cleaned_data['cc_expdate'],
                                     cc_ccv=signup_form.cleaned_data['cc_ccv'])
            new_ubook.save()
        else:
            return render(request, 'website/signUp.html', {
                'error': True,
                'errormsg': "Input Not Valid",
                'form': signup_form
            })

        send_mail('UBook Profile Created!', 'Thanks for joining UBook. Get started saving money on textbook',
                  'ubookautoreply@gmail.com', [signup_form.cleaned_data['email']], fail_silently=False)

        new_user = authenticate(username=signup_form.cleaned_data['username'],
                                password=signup_form.cleaned_data['password'])
        login(request, new_user)

        return HttpResponseRedirect(reverse('index'))

    if request.method == 'GET':
        form = UBookProfileForm()
        return render(request, 'website/signUp.html', {"form": form})


def charge(request):
    if request.method == 'POST':
        # Set your secret key: remember to change this to your live secret key in production
        # See your keys here https://dashboard.stripe.com/account/apikeys
        stripe.api_key = "sk_test_EqcgbisfuVnctYONDROGsHYd"

        amt = int(request.POST['price'])*100;
        profile = UBookProfile.objects.get(user=request.user)

        # Create the charge on Stripe's servers - this will charge the user's card
        try:
            charge = stripe.Charge.create(
                amount=amt,  # amount in cents, again
                currency="usd",
                description="Textbook Bought",
                card={
                    "number": profile.cc_number,
                    "exp_month": profile.cc_expdate[0:2],
                    "exp_year": profile.cc_expdate[3:],
                    "cvc": profile.cc_ccv
                }
            )
            print("Card accepted")
            return JsonResponse({'response': True})
        except Exception as e:
            # The card has been declined
            print(e)
            return JsonResponse({'response': e})

    return HttpResponseRedirect(reverse('index'))
