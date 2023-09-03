from django.shortcuts import render

# Create your views here.
from bsdk.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
#DataFlair #Send Email
def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        name=str(sub['name'].value())
        subject = str(sub['name'].value())
        message = str(sub['phone'].value())+ "\n" + str(sub['message'].value())
        recepient = str(sub['Email'].value())
        send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return redirect("/")
    return render(request, 'contact.html', {'form':sub})