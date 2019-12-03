from django import forms
from users.models import MyUser

# from django.contrib.auth.forms import UserCreationForm
class RegisterForm(forms.ModelForm):

    class Meta:
        model = MyUser
        fields = ('email', 'phone', 'name', 'real_name', 'password')
