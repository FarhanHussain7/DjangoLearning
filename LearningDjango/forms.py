from django import forms

class usersForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(label="Email Address", max_length=100, required=True, widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
    password = forms.CharField(widget=forms.PasswordInput)