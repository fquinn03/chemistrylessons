from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class UserForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = 'Required - 150 characters or fewer. Usernames may contain alphanumeric characters and , _, @, +, . or - '
        self.fields['email'].help_text = 'Required - enter valid email address'
        self.fields['password2'].help_text = 'Enter the same password as before for verification'

    class Meta:
        model = User
        fields = ('username', 'email', 'password1' ,'password2' )

class CustomUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].label = 'User Type'
        self.fields['status'].help_text = 'Select user type'

    class Meta:
        model = CustomUser
        fields = ['status']