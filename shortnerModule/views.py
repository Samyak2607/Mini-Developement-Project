from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ShortUrl, ToDoItem, Library
from .forms import UrlForm, LibraryForm, UserCreateForm
from .shortner import shortner
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

#Chat
from django.utils.safestring import mark_safe
import json



# Create your views here.

def base(request):
	return render(request, 'base.html')

@login_required
def dashboard(request):
	return render(request, 'dashboard.html')

@login_required
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



def registerView(request):
	if(request.method == 'POST'):
		form = UserCreateForm(request.POST)
		if(form.is_valid()):
			form.save()
			return redirect('login_url')
	else:
		form = UserCreateForm()

	return render(request, 'registration/register.html', {'form' : form})

@login_required
def todoView(request):
	to_do_list = ToDoItem.objects.all()

	return render(request, 'todo/todo.html', {'to_do_list':to_do_list})

@login_required
def addToDo(request):

	new_item = ToDoItem(content = request.POST['content'], author = request.user.username)
	if(new_item.content == ''):
		return redirect('todo_url')
	new_item.save()

	return redirect('todo_url') 

@login_required
def deleteTodo(request, todo_id):
	item_to_delete = ToDoItem.objects.get(id = todo_id)
	item_to_delete.delete()
	return redirect('todo_url')

# def weatherView(request):
# 	url = ''
# 	weather_content = 
# 	return render(request, 'weather.html', {'city_weather': weather_content})

@login_required
def upload(request):
	if request.method == 'POST':
		upload_file = request.FILES['document']
		fs = FileSystemStorage()
		name = fs.save(upload_file.name, upload_file)
		context = {
			'url' : fs.url(name)
		}
	return render(request, 'upload/upload.html', context)

def document_list(request):
	doc = Library.objects.all()
	return render(request, 'upload/document_list.html',{'doc':doc})


def document(request):
	if request.method == 'POST':
		form = LibraryForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('document_list_url')
	form = LibraryForm()
	return render(request, 'upload/document.html', {'form':form})


@login_required
def chatView(request):
	return render(request, 'chat/chat.html',{})

def roomView(request, room_name):
	return render(request, 'chat/room.html', {
		'room_name_json':mark_safe(json.dumps(room_name))
		})

