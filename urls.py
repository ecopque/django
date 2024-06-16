"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# python3 manage.py runserver
# python3 manage.py --help

from django.contrib import admin
from django.urls import path
from django.http import HttpResponse #3:

def func_blog(request): #2:
    print('func_blog: xxx')
    return HttpResponse('My func_blog msg.')

def func_home(request):
    print('func_home: yyy')
    return HttpResponse('My func_home msg.')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', func_blog), #1:
    path('', func_home)
]

# python3 manage.py startapp home
# python3 manage.py startapp blog
