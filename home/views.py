from django.shortcuts import render

from home.models import Cv
from . import forms

# Create your views here.

def index(request):
    return render(request, 'home/index.html', {})

def hire(request):
    return render(request, 'home/embaucher.html', {})
def cv(request):
    if request.method == "POST":
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        print(password)
        confirmpassword = request.POST.get('confirmpassword')
        print(confirmpassword)
        firstname = request.POST.get('firstname')

        lastname = request.POST.get('lastname')
        email = request.POST.get('email', '')
        confirmemail = request.POST.get('confirmemail')
        category = request.POST.get('category')
        location = request.POST.get('location')
        cv = request.POST.get('document')

        canadanational = request.POST.get('canadanational')

        savee = Cv(username=username,password=password,confirmpassword=confirmpassword,email=email,confirmemail=confirmemail,firstname=firstname,lastname=lastname,category=category,location=location,cv=cv,)
        savee.save()
        return render(request, 'home/index.html', {})

    return render(request, 'home/cv.html', {})





        # return render(request, 'shop/cv.html')



def work(request):
    return render(request, 'home/travailler.html', {})

def career_center(request):
    return render(request, 'home/centre-de-carriere.html', {})

# Form to receive data
def personal(request):
    if request.method == 'POST':
        form = forms.PersonnelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home/personnel_done.html')
    else:
        form = forms.PersonnelForm

    return render(request, 'home/personnel.html', {'form': form})

