from django import forms
from .models import Keys

class NewKeyForm(forms.ModelForm):
	class Meta:
		model = Keys
		fields = '__all__'

class EmailForm(forms.Form):
    full_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Recipient Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Recipient Email'}))
    otp_code = forms.CharField(max_length=6, widget=forms.TextInput(attrs={'placeholder': 'Enter OTP'}))