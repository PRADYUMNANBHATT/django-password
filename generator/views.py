from django.shortcuts import HttpResponse
from django.shortcuts import render
import random


# Create your views here.
def home(request):
    return render(request,'generator/home.html')
def passwor(request):
  
    characters =list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXY'))
    if request.GET.get('special'):
        characters.extend(list('~!@##$%%^&*()_+'))
    if request.GET.get('number'):
        characters.extend(list('1234567890'))
    length = int(request.GET.get('length'))
    thepassword=""
    for x in range (length):
        thepassword +=random.choice(characters)

    return render(request,'generator/passwor.html',{'password':thepassword})

def about(request):
    return render(request,'generator/about.html')