from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import createuserform,loginform,Addrecordform,updaterecordform
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from .models import Record
from django.contrib import messages

def home(request):
    return render(request,'webapp/index.html')
#...register 
def register(request):

    form = createuserform()

    if request.method == "POST":

        form = createuserform(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Account created successfully!")

            return redirect("my-login")

    context = {'form':form}

    return render(request, 'webapp/register.html', context=context)


#..login

def my_login(request):

    form = loginform()

    if request.method == "POST":

        form = loginform(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)
                messages.success(request, "You Have LoggedIn")

                return redirect("dashboard")

    context = {'form':form}

    return render(request, 'webapp/my-login.html', context=context)


@login_required(login_url='my-login')
def dashboard(request):

    my_records = Record.objects.all()

    context = {'records': my_records}

    return render(request, 'webapp/dashboard.html', context=context)



@login_required(login_url='my-login')
def create_record(request):

    form = Addrecordform()

    if request.method == "POST":

        form = Addrecordform(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Record Created succesfully..!")

            return redirect("dashboard")

    context = {'form': form}

    return render(request, 'webapp/create-record.html', context=context)


@login_required(login_url='my-login')
def update_record(request,pk):
    record=Record.objects.get(id=pk)
    form = updaterecordform(instance=record)
    if request.method=='POST':
        form=updaterecordform(request.POST,instance=record)
        if form.is_valid:
            form.save()
            messages.success(request, "Your record was updated..!")
            return redirect("dashboard")

    context = {'form': form}
    return render(request, 'webapp/update-record.html', context=context)


@login_required(login_url='my-login')
def single_record(request,pk):
    all_record=Record.objects.get(id=pk)
    context = {'record':all_record}

    return render(request, 'webapp/view-record.html', context=context)

def delete_record(request, pk):

    record = Record.objects.get(id=pk)

    record.delete()

    messages.success(request, "Your record was deleted!")

    return redirect("dashboard")

    

def user_logout(request):
    auth.logout(request)
    messages.success(request, "Logout success!")
    return redirect("my-login")