#project/home/settings.py: Por padrão, dentro de "settings.py", no campo "TEMPLATES">'DIRS':[], é um caminho para adicionar novos templates, mas vamos deixar vazio por enquanto.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

#project/home/templates/home.html: Dentro de qualquer app, podemos criar uma pasta chamada "templates" e aqui criar os arquivos que quisermos, neste caso, home.html. Criamos um arquivo "home.html" e dentro dele digitamos exclamação "!" e aparecerá um código html, devemos adicionar entre <body> a linha h1.
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

#project/home/apps.py: Nosso site apresentou erro de "TemplateDoesNotExists at/", então temos que ir na pasta "project/home/app.py" e verificar o "name" e se o código está correto desta forma:
from django.apps import AppConfig
class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

#project/settings.py: Agora você volta no project/settings.py em "INSTALLED_APPS = []" e adiciona 'home', veja abaixo:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
]

#project/home/views.py
from django.http import HttpResponse
from django.shortcuts import render
# def func_home(request):
#     print('func_home: yyy')
#     return HttpResponse('My <b>func_home</b> msg.')
def func_home(request):
    print('func_home: yyy')
    return render(request, 'home.html')
