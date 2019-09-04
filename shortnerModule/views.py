from django.shortcuts import render, redirect
from .models import ShortUrl
from .forms import UrlForm
from .shortner import shortner
# Create your views here.

def home(request):
	form = UrlForm(request.POST)
	temp = ''
	if(request.method == 'POST'):
		if(form.is_valid()):
			new_url = form.save(commit = False)
			temp = shortner().issue_token()
			new_url.short_url = temp
			new_url.save()
		else:
			form = UrlForm()
			temp = 'Invalid URL'

	return render(request, 'home.html', {'form':form, 'temp':temp})	

def destination(request, token):
	long_url = ShortUrl.objects.filter(short_url = token)[0]

	return redirect(long_url.long_url)

