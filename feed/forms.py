from django import forms
from .models import Keys

class NewKeyForm(forms.ModelForm):
	class Meta:
		model = Keys
		fields = '__all__'
