from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
           auth.login(request,user)
           return  redirect('/')
        else:
            messages.info(request,'Invalid Credintiols')
            return redirect('login')


    return render(request,"login.html")

def register(request):
        if request.method== 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password']
            password1 = request.POST['password1']
            if password==password1:
                if User.objects.filter(username=username).exists():
                    messages.info(request,"username taken")
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                     messages.info(request,"emali already exists")
                     return redirect('register')

                else:
                    user=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)

                    user.save();
                    messages.info(request,"user created")
            else:
                messages.info(request,'user not created')
                return redirect('register')
            return redirect('../login/')

        return render(request,"register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')