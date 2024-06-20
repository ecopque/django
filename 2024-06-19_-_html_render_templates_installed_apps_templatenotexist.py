#my_project/project/settings.py: #7:
INSTALLED_APPS = [ #1:
    'django.contrib.admin', #2:
    'django.contrib.auth', #2:
    'django.contrib.contenttypes', #2:
    'django.contrib.sessions', #2:
    'django.contrib.messages', #2:
    'django.contrib.staticfiles', #2:
    'home', #3:
    'blog', #3:
]

#my_project/home/views.py
from django.http import HttpResponse #4:
from django.shortcuts import render #5:
def func_home(request):
    print('func_home: yyy')
    return render(request, 'home/index.html') #6:
#my_project/blog/views.py:
from django.http import HttpResponse
from django.shortcuts import render
def func_blog(request):
    print('func_blog: xxx')
    return render(request, 'blog/index.html')
def func_example(request):
    print('func_blog: xxx2')
    return render(request, 'blog/example.html')

#my_project/home/templates/home/index.html: 
<!DOCTYPE html> #8: #9: #10:
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Doc Home</title>
</head>
<body>
    <h1>HOME.html</h1>
</body>
</html>
#my_project/blog/templates/blog/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Doc Blog</title>
</head>
<body>
    <h> HOME_blog.html</h>
</body>
</html>
#my_project/blog/templates/blog/example.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h>EXAMPLE.html</h>
</body>
</html>

#my_project/home/apps.py: 
from django.apps import AppConfig #11:
class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
#my_project_blog/apps.py
from django.apps import AppConfig
class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
