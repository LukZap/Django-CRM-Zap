from .models import Company, Customer_Assistant
from django.contrib.auth.models import User
from django import forms

class CompanyAddForm(forms.ModelForm):
    name = forms.CharField(label='Nazwa firmy')
    phone_number = forms.CharField(label='Numer telefonu')
    adress = forms.CharField(label='Adres')
    adnotations = forms.CharField(widget=forms.Textarea,label='Notatki')
    class Meta:
        model = Company
        fields = ('name', 'NIP', 'phone_number','adress','logo','adnotations')

class CustomerAssistEditForm(forms.ModelForm):
    photo = forms.ImageField(label='Zdjęcie')
    phone_number = forms.CharField(label='Numer telefonu')
    date_birth = forms.DateField(label='Data urodzenia')
    class Meta:
        model = Customer_Assistant
        fields = ('photo','phone_number', 'date_birth')

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class CompanyEditForm(forms.ModelForm):
    name = forms.CharField(label='Nazwa firmy')
    phone_number = forms.CharField(label='Numer telefonu')
    adress = forms.CharField(label='Adres')
    adnotations = forms.CharField(widget=forms.Textarea,label='Notatki')
    class Meta:
        model = Company
        fields = ('name', 'NIP', 'phone_number','adress','logo','adnotations')

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Hasło',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Powtórz hasło',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Hasła nie są identyczne.')
        return cd['password2']
