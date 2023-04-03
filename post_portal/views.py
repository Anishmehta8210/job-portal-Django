from django.shortcuts import render
from .models import *
from random import randint


# Create your views here.

def home(r):
    return render(r,"app/index.html")


def signup(r):
    return render(r,"app/signup.html")


def RegisterUser(r):
    if r.POST['role'] == "Candidate":
        role = r.POST['role']
        fname = r.POST['first_name']
        lname = r.POST['last_name']
        email = r.POST['email']
        password = r.POST['password']
        cpassword = r.POST['cpassword']

        user= UserMaster.objects.filter(email=email)

        if user:
            message = "User already Exist"
            return render (r,"app/signup.html",{'msg':message})
        
        else:
            if password == cpassword:
                otp = randint(100000,999999)
                newuser = UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
                newcand = UserMaster.objects.create(user_id = newuser,first_name=fname,last_name=lname)
                return render (r,"app/otpverify.html")

    else:
        pass





