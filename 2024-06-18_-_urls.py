#urls.py (blog/new)
from django.contrib import admin
from django.urls import path
from blog import views as blog_views
urlpatterns = [
    path('', blog_views.func_blog),
    path('example', blog_views.func_example)
]

#urls.py (home/new)
from django.contrib import admin
from django.urls import path
from home import views as home_views
urlpatterns = [
    path('', home_views.func_home),
]

#urls.py (.)
from django.contrib import admin
from django.urls import path
# from home import views as home_views
# from blog import views as blog_views
from django.urls import include #
urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')), 
]

#views.py (blog)
from django.http import HttpResponse
def func_blog(request):
    print('func_blog: xxx')
    return HttpResponse('My func_blog msg.')
def func_example(request):
    print('func_blog: xxx2')
    return HttpResponse('My func_example msg')

#views.py (home)
from django.http import HttpResponse
def func_home(request):
    print('func_home: yyy')
    return HttpResponse('My func_home msg.')
