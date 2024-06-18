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
# python3 manage.py runserver #1:
# python3 manage.py --help #2:
# python3 manage.py startapp home #3:
# python3 manage.py startapp blog #3:

# urls.py
from django.contrib import admin #4:
from django.urls import path #4:

from blog import views as blog_views #5:
from home import views as home_views #5:

urlpatterns = [ #6:
    path('admin/', admin.site.urls), #7:
    path('blog/', blog_views.func_blog), #8:
    path('', home_views.func_home) #9:
]
#../blog/views.py
from django.http import HttpResponse #10:

def func_blog(request):
    print('func_blog: xxx')
    return HttpResponse('My func_blog msg.')

#../home/views.py
from django.http import HttpResponse #10:

def func_home(request):
    print('func_home: yyy')
    return HttpResponse('My func_home msg.')
