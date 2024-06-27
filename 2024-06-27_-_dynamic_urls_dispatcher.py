#my_project/urls.py:

from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('', include('home.urls')), #my_project/home/urls.py
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')), #my_project/blog/urls.py
]

#my_project/blog/urls.py:

from django.urls import path
from blog import views as blog_views #my_project/blog/views.py

app_name = 'blog'
urlpatterns = [
    path('', blog_views.func_blog, name='blog_home'), #my_project/blog/views.py
    path('post/<int:id>/', blog_views.func_post, name='blog_post'), #my_project/blog/views.py
    path('example/', blog_views.func_example, name='blog_example'), #my_project/blog/views.py
]

#my_project/blog/views.py:

from django.shortcuts import render
from blog.data import var_posts #my_project/blog/data.py

def func_blog(request):
    print('func_blog: blog/views.py')
    var_context = {
        'key_text': 'We are home: blog',
        'key_posts': var_posts #my_project/blog/data.py
        }
    return render(request, 'blog/index.html', context=var_context)

def func_post(request, id):
    print('func_post: url: /blog/post/x=', id)
    var_context = {
        'key_posts': var_posts #my_project/blog/data.py
    }
    return render(request, 'blog/index.html', context=var_context)

def func_example(request):
    print('func_example: blog/views.py')
    return render(request, 'blog/example.html')

{#my_project/blog/templates/blog/index.html:#}

{% extends 'global/base.html' %} {#my_project/base/global/base.html#}
{% block text %} {{key_text}} {% endblock text %} {#my_project/blog/views.py#}

{% block posts %}
    {% for var_post in key_posts %} {#my_project/blog/views.py#}
        {% include 'global/partials/postblock.html' %} {#my_project/base/global/partials/postblock.html#}
    {% endfor %}
{% endblock posts %}

{#my_project/base/global/base.html#}

{% include 'global/partials/head.html' %} {#my_project/base/global/partials/head.html#}
{% include 'global/partials/menu.html' %} {#my_project/base/global/partials/menu.html#}

{% if key_text %} {#my_project/blog/views.py#}
    <h1>{% block text %}{% endblock text %}</h1>
{% endif %}

<main class="content">
    {% block posts %}{% endblock posts %}
    {% block home %}{% endblock home %}
</main>

</body>
</html>

{#my_project/base/global/partials/menu.html:#}

<nav>
    <ul>
        <li>
            <a href="{% url 'home_home' %}">Home</a> {#my_project/home/urls.py#}
        </li>
        <li>
            <a href="{% url 'blog:blog_home' %}">Blog</a> {#my_project/blog/urls.py#}
        </li>
        <li>
            <a href="{% url 'blog:blog_example' %}">Example</a> {#my_project/blog/urls.py#}
        </li>
    </ul>
</nav>

{#my_project/base/global/partials/head.html:#}

{% load static %} <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{% static 'global/css/style.css' %}"> {#my_project/base/static/global/css/style.css#}
</head>
<body>
    <h1>Mensagem do HEAD.HTML</h1>

{#my_project/base/global/partials/postblock.html:#}

<article class="post">
    <header>
        <h2 class="post__title">
            <a href="{% url "blog:blog_post" var_post.id %}"> {#my_project/blog/urls.py#} | {#my_project/blog/data.py#}
                {{var_post.title}} {#my_project/blog/data.py#}
            </a>
        </h2>
    </header>
    <div class="post__body">
        {{var_post.body}} {#my_project/blog/data.py#}
    </div>
</article>

#my_project/blog/data.py:

var_posts = [
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
  } (...)
