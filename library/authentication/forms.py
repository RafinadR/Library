from django import forms
from .models import CustomUser
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import UserCreationForm



class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    


class UserRegistrationForm(UserCreationForm):
    class Meta:   
        model = CustomUser
        fields = ['email', 'password1', 'password2', 'first_name', 'middle_name', 'last_name', 'role']
        widgets = { 'email': forms.EmailInput()}
        help_texts = {
            'email':'Your email must contain @.',
            'middle_name': 'Optional '
        }
        
        
        
    
    def clean_email(self):
        """
        Custom validation to check for unique email addresses.
        """
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("Email address already exists. Please choose a different one.")
        return email
        