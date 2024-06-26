#my_project/blog/views.py:
from django.shortcuts import render
from blog.data import var_posts

def func_blog(request):
    print('func_blog: blog/views.py')
    var_context = {
        'key_text': 'We are home: blog',
        'key_posts': var_posts
        }
    return render(request, 'blog/index.html', context=var_context)

def func_example(request):
    print('func_example: blog/views.py')
    return render(request, 'blog/example.html')

#my_project/blog/templates/blog/index.html:
{% extends 'global/base.html' %}
{% block text %} {{key_text}} {% endblock text %}

{% block posts %}
    {% for var_post in key_posts %}
        {% include 'global/partials/postblock.html' %}
    {% endfor %}
{% endblock posts %}

#my_project/base/global/base.html:
{% include 'global/partials/head.html' %}
{% include 'global/partials/menu.html' %}

{% if key_text %} #1:
    <h1>{% block text %}{% endblock text %}</h1> #1:
{% endif %} #1:

<main class="content">
    {% block posts %}{% endblock posts %}
    {% block home %}{% endblock home %}
</main>

</body>
</html>
