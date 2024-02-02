from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from farmapp.models import Product1,Sellproduct
from django.contrib import messages
#from .forms import ProductAvailabilityForm
#from .models import UserProfile
#from django.views.decorators.csrf import csrf_exempt
#from django.db import IntegrityError

def signuppage(request): 
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("your password and confirm password are not same")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render(request,'signup.html')

def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('f1')
    
        else:
            return HttpResponse("username or password is incorrect")
    return render(request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')
@login_required(login_url='login')
def f1y(request):
    p1=Product1.objects.filter(page=1).distinct
    return render(request,'project1.html',{'products':p1}) 
    return render(request,'project1.html',{'user':request.user})
   
def f2w(request):
    p2=Product1.objects.filter(page=2).distinct
    return render(request,'project 2.html',{'products':p2}) 
def f3s(request):
    p3=Product1.objects.filter(page=3).distinct
    return render(request,'summercrops.html',{'products':p3}) 
def f4c(request):
    return render(request,'contactus.html')

def p(request):
    return render(request,'product_sell_form.html')

def create_product(request):
    if request.method == 'POST':
        # Retrieve data from the request
        name = request.POST['name']
        location = request.POST['location']
        quantity = request.POST['quantity']
        date = request.POST['date']
        phone_number = request.POST['phone_number']

        # Create and save a new Product instance
        product = Sellproduct(
            name=name,
            location=location,
            quantity=quantity,
            date=date,
            phone_number=phone_number,
        )
        product.save()
        

        # Redirect to a success page or another appropriate view
        #return redirect('f1')  # Change 'success_page' to the URL name of your success page

    return render(request, 'result.html')

