#my_project/project/settings.py:
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'base' #1:
        ],
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

#my_project/home/views.py:
from django.shortcuts import render
def func_home(request):
    print('func_home: yyy')
    return render(request, 'global/base.html') #2:

#my_project/base/global/base.html:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>{% block text %} BASE {% endblock text %}</h1> #3:
</body>
</html>

#########################

#my_project/home/views.py:
from django.shortcuts import render
def func_home(request):
    print('func_home: yyy')
    return render(request, 'home/index.html') #4:

#my_project/home/templates/home/index.html:
{% extends 'global/base.html' %} #5:
{% block text %} CHANGE TEXT {% endblock text %} #6:
