#******************************
#my_project/project/settings.py: Agora você volta no project/settings.py em "INSTALLED_APPS = []" e adiciona 'home', veja abaixo:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'blog',
]

#************************
#my_project/home/views.py
from django.http import HttpResponse
from django.shortcuts import render
def func_home(request):
    print('func_home: yyy')
    return render(request, 'home/index.html')
#my_project/blog/views.py:
from django.http import HttpResponse
from django.shortcuts import render
def func_blog(request):
    print('func_blog: xxx')
    return render(request, 'blog/index.html')
def func_example(request):
    print('func_blog: xxx2')
    return render(request, 'blog/example.html')

#*****************************************
#my_project/home/templates/home/index.html: Dentro de qualquer app, podemos criar uma pasta chamada "templates" e aqui criar os arquivos que quisermos, neste caso, index.html.
# #Obs: Coloque estes arquivos dentro da pasta de mesmo nome do app, para evitar conflitos. 
# #Continua: Criamos um arquivo "index.html" e dentro dele digitamos exclamação "!" e aparecerá um código html, devemos adicionar entre <body> a linha <h1>.
<!DOCTYPE html>
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

#***********************
#my_project/home/apps.py: Nosso site apresentou erro de "TemplateDoesNotExists at/", então temos que ir na pasta "project/home/app.py" e verificar o "name" e se o código está correto desta forma:
from django.apps import AppConfig
class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
#my_project_blog/apps.py
from django.apps import AppConfig
class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
