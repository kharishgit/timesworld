from django import forms
from .models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['first_name','country','nationality','phone_number','role','last_name', 'email', 'password']


    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if any(char.isdigit() or not char.isalnum() for char in first_name):
            raise forms.ValidationError("First name should not contain special characters or digits.")
        return first_name

    def clean_email(self):
        email = self.cleaned_data['email']
        
        if not email or "@" not in email:
            raise forms.ValidationError("Enter a valid email address.")
        return email

    

    
    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        print(cleaned_data)
        password = cleaned_data['password']
        if len(password) < 6:
            raise forms.ValidationError("Password Must Contains at least 6 characters")
        confirm_password = cleaned_data['confirm_password']
        mobile = cleaned_data.get('phone_number')
        if confirm_password != password:
            raise forms.ValidationError("Password Do not match")
        if not mobile.isdigit() or len(mobile) != 10:
            raise forms.ValidationError("Mobile Number not valid.")
        
       
        return cleaned_data
