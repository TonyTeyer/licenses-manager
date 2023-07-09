from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.models import User
from .models import Licenses
from .forms import LicensesForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# No login required-----
def home(request):
    return render(request, 'home.html')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Inocrrect Username or Password'
            })
        else:
            login(request, user)
            return redirect('licenses')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm  # to render the form
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('licenses')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Username already exist'  # error manage
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Password do not match'  # error manage
        })


# login Required----------
@login_required
def licenses(request):
    license = Licenses.objects.filter(user=request.user)
    return render(request, 'licenses.html', {
        'licenses': license
    })


@login_required
def signout(request):
    logout(request)
    return redirect('home')


@login_required
def form_licenses(request):
    if request.method == 'GET':
        return render(request, 'form_licenses.html', {
            'form': LicensesForm
        })
    else:
        try:
            form = LicensesForm(request.POST)
            # Create a new License object from the form data, but don't save it to the database yet
            new_license = form.save(commit=False)
            # Set the user of the license as the current user
            new_license.user = request.user
            # Save the license object to the database
            new_license.save()
            return redirect('licenses')
        except ValueError:
            return render(request, 'form_licenses.html', {
                'form': LicensesForm,
                'error': 'Please fill in all required fields.'
            })


@login_required
def license_detail(request, license_id):
    license = get_object_or_404(Licenses, pk=license_id)
    return render(request, 'license_detail.html', {
        'license': license,
    })


@login_required
def update_license(request, license_id):
    license = get_object_or_404(Licenses, pk=license_id)
    if request.method == 'POST':
        form = LicensesForm(request.POST, instance=license)
        if form.is_valid():
            form.save()
            return redirect('license_detail', license_id=license_id)
    else:
        form = LicensesForm(instance=license)
    return render(request, 'update_license.html', {
        'license': license,
        'form': form,
    })


@login_required
def delete_license(request, license_id):
    license = get_object_or_404(Licenses, pk=license_id, user=request.user)
    if request.method == 'POST':
        license.delete()
        return redirect('licenses')
