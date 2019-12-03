from django import forms
from core.models import ContactUs
from core.utils import phone_formatting
from core.validators import name_validator


class PhoneFormMixin(forms.Form):
    phone = forms.CharField(max_length=20)

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        phone = phone_formatting(phone)
        if len(phone) != 12:
            raise forms.ValidationError('Неверный формат телефона')
        return phone


class ContactUsForm(forms.ModelForm, PhoneFormMixin):
    name = forms.CharField(label='Имя', max_length=128, validators=[name_validator])
    comment = forms.CharField(max_length=255, widget=forms.Textarea({'rows': 2, 'cols': 20}), required=False)

    class Meta:
        model = ContactUs
        fields = '__all__'

    def clean_email(self):
        email = self.cleaned_data["email"]
        if len(email) < 10:
            raise forms.ValidationError('not valid length')
        return email
