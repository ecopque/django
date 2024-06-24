#my_project/home/views.py:
from django.shortcuts import render
def func_home(request):
    print('func_home: yyy')
    var_context = {'key_text': 'We are home!'}
    return render(request, 'home/index.html', context=var_context) #1:

#my_project/home/templates/home/index.html:
{% extends 'global/base.html' %}
{% block text %} #2:
    {{ key_text }} #2:
{% endblock text %} #2:
