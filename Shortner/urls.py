"""Shortner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
# from djangopush.views import signInView, After_signIn
from django.contrib.auth import views as auth_views
from shortnerModule.views import upload, document, document_list, chatView, roomView
from shortnerModule.views import home, destination, base, registerView, dashboard, todoView, addToDo, deleteTodo
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
	path('',base, name = 'base_url'),
    path('admin/', admin.site.urls),
    path('url-shortner/', home, name= 'short_url'),
    path('<str:token>', destination, name = 'destiny'),
    path('dashboard/', dashboard, name = 'dashboard_url'),
    path('login/',LoginView.as_view(), name = 'login_url'),
    path('register/', registerView, name = 'register_url'),

    path('library/update/', document, name = 'document_update_url'),
    path('library/', document_list, name = 'document_list_url'),

    path('upload/', upload, name = 'upload_url'),
    path('todo-list/', todoView, name = 'todo_url'),
    path('add-to-do/', addToDo, name = 'add_todo_url'),
    path('delete-to-do/<int:todo_id>/', deleteTodo, name = 'delete_url'),

    path('chat/', chatView, name = 'chat_url'),
    path('chat/<str:room_name>/', roomView, name = 'room_url'),

    path('logout/', LogoutView.as_view(next_page = 'base_url'), name = 'logout'),


    #django-firebase

    # path('sign_in/', signInView, name = 'login_url'),
    # path('login_action/', AfterLoginView, name = 'after_login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
