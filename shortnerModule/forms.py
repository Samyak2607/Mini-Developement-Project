from django import forms
from .models import ShortUrl, Library
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreateForm(UserCreationForm):
	email = forms.EmailField(required=True,label='Email',error_messages={'exists': 'Oops'})
	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")
	def clean_email(self):
		email = self.cleaned_data.get('email')
		username = self.cleaned_data.get('username')
		if email and User.objects.filter(email=email).exclude(username=username).exists():
			raise forms.ValidationError(u'Email addresses must be unique.')
		return email

    

class UrlForm(forms.ModelForm):
	class Meta:
		model = ShortUrl
		fields = ['long_url']

class  LibraryForm(forms.ModelForm):
	class Meta:
		model = Library
		fields = ('title', 'author', 'document', 'cover')


# class EmailVerification(forms.ModelForm):
# 	email = forms.EmailField(label="", widget=forms.EmailInput(attrs = {
# 		'placeholder': 'Enter Email ID',
# 		}), max_length = 120, error_messages={'invalid': ("Email invalide.")},validators=[isValidEmail])

# 	def 
			
