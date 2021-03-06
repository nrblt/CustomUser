# from pyexpat.errors import messages
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
from users.forms import CustomUserCreationForm, DevicesForm
from users.models import Devices


def registrationPage(request):
    if request.user.is_authenticated:
        context = {'a': 1}

        return redirect(forLogged)
    else :
        form = CustomUserCreationForm()
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('login')

                # messages.success(request, "Everything is GOOD " + user)
                return redirect(loginPage)
                # return HttpResponse('YOU Registered')
            else:
                messages.info(request, "Something is wrong")

        context = {'form': form}
        return render(request, 'registration.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect(forLogged)
    else:
        if request.method == 'POST':
            login1 = request.POST.get('login')
            password = request.POST.get('password')
            user = authenticate(request, login=login1, password=password)
            if user is not None:
                login(request, user)
                # return redirect(index)
                return redirect(forLogged)
            else:
                messages.info(request, "Something is wrong with your login of password")

        context = {}
        return render(request, 'login.html', context)


@login_required(login_url='login')
def forLogged(request):
    # allDevices=Devices.objects.get(user=request.user)
    allDevices=Devices.objects.all().filter(user=request.user)
    form=DevicesForm()
    if request.method=='POST':
        # user = request.user
        # ESN = request.POST.get('ESN')
        # form = DevicesForm(initial={'user': request.user})
        # tank = forms.IntegerField(widget=forms.HiddenInput(), initial=123)
        # form(request,pet=pet,user=request.user)
        # return redirect(logoutUser)
        # form.fields['user'].initial = request.user
        form=DevicesForm(request.POST)
        if form.is_valid()==True:
            # return redirect(logoutUser)
            device=form.save(commit=False)
            device.user=request.user
            device.save()
            # form.save()
        return redirect(forLogged)

    context = {
        'form': form,
        'devices' : allDevices,
    }
    return render(request,'forlogged.html',context)
    # try :
    #     allDevices = Devices.objects.all().filter(user=request.user)
    #
    # except:
    #     allDevices=['nothing']
    #
    # context={
    # #
    #     'devices':allDevices
    # }
    # return render(request,'forlogged.html',context)


def logoutUser(request):
    logout(request)
    return redirect(loginPage)

def deleteDevice(request,pk):
    device = Devices.objects.get(id=pk)
    device.delete()
    return redirect(forLogged)
#Biba2281537

def updateDevice(request,pk):
    device  = Devices.objects.get(id=pk)
    form    = DevicesForm(instance=device)
    if request.method == 'POST':
        form = DevicesForm(request.POST, instance=device)
        if form.is_valid():
            form.save()
            return redirect(forLogged)

    context = {
        'form': form,
        'device': device
    }
    return render(request, 'update_device.html', context)

