from django.http import HttpResponse
from django.shortcuts import render,redirect
import datetime

def redirect_to_home(request):
    return redirect(home)

def home(request):
    return render(
        request,
        'hello.html',
        {
            'date': datetime.datetime.now()
        })

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')




