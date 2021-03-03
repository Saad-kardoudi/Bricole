from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Account
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .filters import *
# Create your views here.
def index(request):
    return render(request, 'home/index.html')


def Login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username', 'null')
        password = request.POST.get('password', 'null')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    context = {}
    return render(request, 'home/login.html', context)


def Logout_page(request):
    logout(request)
    return redirect('Login')


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    form1 = CreationUserForm()
    if request.method == 'POST':
        form1 = CreationUserForm(request.POST)
        if form1.is_valid():
            form1.save()
            userx = User.objects.get(username=request.POST.get('username', 'null'))
            return redirect('register2', userx.pk)
        else:
            print("form 1 isn't valid")
            print("--------------------------------------")
            print(form1.errors)
            print("--------------------------------------")
    context = {'form1': form1}
    return render(request, 'home/register.html', context)


def register2(request, pk):
    if request.user.is_authenticated:
        return redirect('home')
    form2 = CreationAccountForm()
    if request.method == 'POST':
        form2 = CreationAccountForm(request.POST)
        if form2.is_valid():
            form2.save()
            userx = User.objects.get(pk=pk)
            messages.success(request, 'Account was created for '+userx.first_name+' '+userx.last_name)
            return redirect('Login')
        else:
            print("form 2 isn't valid")
            print("--------------------------------------")
            print(form2.errors)
            print("--------------------------------------")
    context = {'pk': pk, 'form2': form2}
    return render(request, 'home/register2.html', context)


def home(request):
    acconts = Account.objects.all()
    #filterjob = AccontFilter()
    context = {'acconts': acconts}
    return render(request, 'home/home.html', context)


@login_required(login_url='Login')
def MyAccount(request):
    user = request.user
    account = Account.objects.get(user=user)
    comments = Rating.objects.filter(Worker=account)
    context = {'user': user, 'account': account, 'comments': comments}
    return render(request, 'home/your_Account.html', context)


@login_required(login_url='Login')
def edit_MyAccount(request):
    user = request.user
    account = Account.objects.get(user=user)
    comments = Rating.objects.filter(Worker=account)
    form1 = EditionUserForm(instance=user)
    form2 = EditAccountForm(instance=account)
    if request.method == 'POST':
        form1 = EditionUserForm(request.POST, instance=user)
        form2 = EditAccountForm(request.POST, request.FILES, instance=account)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return redirect('MyAccount')
        else:
            print("--------------------------------------")
            print(form1.errors)
            print("--------------------------------------")
            print(form2.errors)
            print("--------------------------------------")
    context = {'user': user, 'account': account, 'form1': form1, 'form2': form2, 'comments': comments}
    return render(request, 'home/edit_MyAccount.html', context)


@login_required(login_url='Login')
def Account_page(request, pk):
    user = User.objects.get(pk=pk)
    if request.user == user:
        return redirect('MyAccount')
    employee = Account.objects.get(user=request.user)
    account = Account.objects.get(user=user)
    comments = Rating.objects.filter(Worker=account)
    form = CreationRatingForm()
    if request.method == 'POST':
        form = CreationRatingForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("--------------------------------------")
            print(form.errors)
            print("--------------------------------------")
    context = {'user': user, 'account': account, 'form': form, 'employee': employee, 'comments': comments}
    return render(request, 'home/your_Account.html', context)

