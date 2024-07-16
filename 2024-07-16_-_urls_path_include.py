# Criamos apps chamados "urls.py" nos apps (pastas blog e home).
#urls.py (.)
from django.contrib import admin #1:
from django.urls import path #2:
# from home import views as home_views
# from blog import views as blog_views
from django.urls import include #3:
urlpatterns = [
    path('', include('home.urls')), #4:
    path('admin/', admin.site.urls), #5:
    path('blog/', include('blog.urls')), #6:
]
#urls.py (blog/new)
from django.contrib import admin
from django.urls import path
from blog import views as blog_views #7:
urlpatterns = [
    path('', blog_views.func_blog), #8:
    path('example', blog_views.func_example) #9: #10:
]
#views.py (blog)
from django.http import HttpResponse #11:
def func_blog(request):
    print('func_blog: xxx')
    return HttpResponse('My func_blog msg.') #12:
def func_example(request):
    print('func_blog: xxx2')
    return HttpResponse('My func_example msg')
#urls.py (home/new)
from django.contrib import admin
from django.urls import path
from home import views as home_views
urlpatterns = [
    path('', home_views.func_home),
]
#views.py (home)
from django.http import HttpResponse
def func_home(request):
    print('func_home: yyy')
    return HttpResponse('My func_home message.')
