from django import forms
from .models import Keys

class NewKeyForm(forms.ModelForm):
	class Meta:
		model = Keys
		fields = '__all__'

class EmailForm(forms.Form):
    full_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Customer Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Customer Email'}))
    vehicle_info = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Vehicle Details'}))
    key_code = forms.CharField(max_length=6, widget=forms.TextInput(attrs={'placeholder': 'Enter Key Code'}))