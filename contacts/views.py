from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from . import forms

def contact(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['name']
            comment = form.cleaned_data['comment']
            subject = 'Message from MYSITE.com'
            message =  '%s %s' %(comment, name)
            emailFrom = form.cleaned_data['email']
            emailTo = [settings.EMAIL_HOST_USER]
        form = False
        title = 'Thanks!'
        context = {'title':title, 'form':form}    
        messages.success(request, 'Thanks for the message. We will get right back to you.')
        return render(request, 'contacts/contact.html', context)
    else:
        title = 'Contact'
        form = forms.ContactForm()
        context = {'title':title, 'form':form}
        return render(request,'contacts/contact.html', context)

