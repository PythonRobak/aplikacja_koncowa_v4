from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError, ObjectDoesNotExist

from webadminpanel.models import Media, Group, Player


def login_validator(value):
    try:
        User.objects.get(username=value)

    except ObjectDoesNotExist:
        raise ValidationError('You have entered an invalid username!')


class LoginForm(forms.Form):

    username = forms.CharField(label="Login:", max_length=50, required=True)
    password = forms.CharField(label="Password:", widget=forms.PasswordInput())

def email_validator(value):
    if User.objects.get(email=value) == value:
        raise ValidationError('This email is already in the database!')


class AddUserForm(forms.ModelForm):
    password1 = forms.CharField(label="password1", widget=forms.PasswordInput())
    password2 = forms.CharField(label="password2", widget=forms.PasswordInput())
    field_order = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'phone_number']

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number']

class AddMediaForm(forms.ModelForm):

    class Meta:
        model = Media
        fields = ['name', 'file', 'duration']

class AddGroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ['name', 'description']


class AddPlayerForm(forms.ModelForm):
    # status = forms.IntegerField(label="status")

    field_order = ['name', 'description', 'number_of_screens', 'geo_longitude', 'geo_latitude', 'country', 'state',
              'city', 'street', 'street_number', 'building_number', 'status', 'groups']

    class Meta:
        model = Player
        fields = ['name', 'description', 'number_of_screens', 'geo_longitude', 'geo_latitude', 'country', 'state',
                  'city','street', 'street_number', 'building_number', 'status', 'groups']



