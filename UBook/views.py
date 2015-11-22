from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render

from .models import User
from UBook.models import UBookProfile, UBookProfileForm

def index(request):
    return render(request, 'website/index.html', {})

def about(request):
    return render(request, 'website/about.html', {})

def signup(request):

    if request.method == 'POST':
        """
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        cc_type = request.POST['cc_type']
        cc_number = request.POST['cc_number']
        cc_expdate = request.POST['cc_expdate']
        cc_ccv = request.POST['cc_ccv']
        """

        signup_form = UBookProfileForm(request.POST)
       
        if signup_form.is_valid():
            new_user = User.objects.create_user(username=signup_form.cleaned_data['username'], 
                password=signup_form.cleaned_data['password'], 
                email=signup_form.cleaned_data['email'], 
                first_name=signup_form.cleaned_data['first_name'], 
                last_name=signup_form.cleaned_data['last_name'])

            new_ubook = UBookProfile(user=new_user, 
                address=signup_form.cleaned_data['address'], 
                city=signup_form.cleaned_data['city'], 
                state=signup_form.cleaned_data['state'], 
                zipcode=signup_form.cleaned_data['zipcode'], 
                cc_type=signup_form.cleaned_data['cc_type'], 
                cc_number=signup_form.cleaned_data['cc_number'], 
                cc_expdate=signup_form.cleaned_data['cc_expdate'], 
                cc_ccv=signup_form.cleaned_data['cc_ccv'])
            new_user.save()
            new_ubook.save()
            return HttpResponseRedirect(reverse('index'))

        else:
            print("FUCKIN SHIT UP")
            print(signup_form.errors)
            return render(request, 'website/signUp.html', {
                'error':True,
                'errormsg':"Input Not Valid",
                'form':signup_form
            })




    if request.method == 'GET':
        form = UBookProfileForm()
        return render(request, 'website/signUp.html', {"form":form})

