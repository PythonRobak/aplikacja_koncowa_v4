from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

# Create your views here.

from webadminpanel.forms import LoginForm, AddUserForm, AddMediaForm
from webadminpanel.models import Media


class LoginUserView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'webadminpanel/login.html', {'form': form})

    def post(self, request):

        form = LoginForm(request.POST)
        msg = "You have entered an invalid username!"
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:

                login(request, user)
                return render(request, 'webadminpanel/logged_in.html', {'form': form, 'msg': msg})

            else:

                msg = "You have entered an invalid password!"

        return render(request, 'webadminpanel/login.html', {'form': form, 'msg': msg})

class LogoutUserView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


class AddUserView(View):
    def get(self, request):
        form = AddUserForm()
        return render(request, 'webadminpanel/add-user.html', {'form': form})

    def post(self, request):
        form = AddUserForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password1'] != form.cleaned_data['password2']:
                msg = 'Password didnt match!'
                return render(request, 'webadminpanel/add-user.html', {'form': form, 'msg': msg})


            u = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                password=form.cleaned_data['password1']

            )

            return redirect('users')

        return render(request, 'webadminpanel/logged_in.html', {'form': form})

class LoggedInView(View):
    def get(self, request):
        return redirect('logged-in')

class UsersView(View):
    def get(self, request):
        users = User.objects.all().order_by('last_name')
        ctx = {
            'users': users
        }
        return render(request, 'webadminpanel/users.html', ctx)


class AddMediaView(View):
    def get(self, request):
        form = AddMediaForm()
        return render(request, 'webadminpanel/add-media.html', {'form': form})

    def post(self, request):
        form = AddMediaForm(request.POST, request.FILES or None)
        print("*"*50)

        if form.is_valid():
            print("media form validated")
            media = Media()
            media.name = form.cleaned_data['name']
            media.file = form.cleaned_data['file']

            try:
                # media = Media.objects.create(
                #     name=form.cleaned_data['name'],
                #     file=form.cleaned_data['file'],
                #     duration=duration.form.cleaned_data['duration']
                # )
                media = Media()
                media.name = form.cleaned_data['name']
                media.file = form.cleaned_data['file']
                # media.file = request.POST.get('file')
                media.duration = form.cleaned_data['duration']

                media.save()
                

                return redirect('media')

            except Exception:
                return HttpResponse("Something went wrong!")

        else:
            print("media form not validated!")
            print("Błąd formularza:")
            print(form.errors)
        return render(request, "webadminpanel/media.html", {'form': form})

class MediaView(View):
    def get(self, request):
        media = Media.objects.all()
        ctx = {
            'media': media
        }
        return render(request, 'webadminpanel/media.html', ctx)

