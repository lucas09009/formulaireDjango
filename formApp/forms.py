from django import forms
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password', 
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        
    )

    password2 = forms.CharField(
        label='Confirm Password', 
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('password1', 'password2')
        help_texts = {  # 👇 ici on écrase les help_texts
            'username': None,
            'password1': None,
            'password2': None,
        }
    

    # class ContactForm(forms.Form):
    #     name = forms.CharField(max_length=100, required=True, label='name'),
    #     email = forms.EmailField(required=True, label='Email Address'),
    #     messsage = forms.CharField(widget=forms.Textarea, required=True, label='Message')
    #     password = forms.CharField(widget=forms.PasswordInput, required=True, label='Password'),
    #     confirm_password = forms.CharField(widget=forms.PasswordInput, required=True, label='confirm_password')