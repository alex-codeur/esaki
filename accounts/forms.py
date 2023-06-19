from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label='username', max_length=250, min_length=3, help_text='', required=True, widget=forms.TextInput(attrs={"type":"text", "id":"username", "class":"bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500", "placeholder":"Username"}))
    first_name = forms.CharField(label='first_name', max_length=250, min_length=3, help_text='', required=True, widget=forms.TextInput(attrs={"type":"text", "id":"first_name", "class":"bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500", "placeholder":"First Name"}))
    last_name = forms.CharField(label='last_name', max_length=250, min_length=3, help_text='', required=True, widget=forms.TextInput(attrs={"type":"text", "id":"last_name", "class":"bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500", "placeholder":"Last Name"}))
    email = forms.CharField(label='email', max_length=250, min_length=5, help_text='', required=True, widget=forms.TextInput(attrs={"type":"email", "id":"email", "class":"bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500", "placeholder":"Email"}))
    password = forms.CharField(label='password', max_length=250, min_length=8, help_text='', required=True, widget=forms.TextInput(attrs={"type":"password", "id":"password", "class":"bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500", "placeholder":"Mot de passe"}))
    confirm_password = forms.CharField(label='confirm_password', max_length=250, min_length=8, help_text='', required=True, widget=forms.TextInput(attrs={"type":"password", "id":"confirm_password", "class":"bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-indigo-600 focus:border-indigo-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500", "placeholder":"Mot de passe"}))
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']