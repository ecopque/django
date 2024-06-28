#my_project/blog/urls.py:

from django.urls import path
from blog import views as blog_views #my_project/#my_project/blog/views.py:

from django.shortcuts import render
from blog.data import var_posts #my_project/blog/data.py
from django.http import Http404

def func_blog(request):
    print('func_blog: blog/views.py')
    var_context = {
        'key_text': 'We are home: blog',
        'key_posts': var_posts #my_project/blog/data.py
        }
    return render(request, 'blog/index.html', context=var_context)

def func_post(request, post_id):
    print('func_post: url: /blog/post/x=', post_id)
    var_foundpost = None
    for i_post in var_posts:
        if i_post['id'] == post_id:
            var_foundpost = i_post
            break
    if var_foundpost is None:
        raise Http404('Error 404: page does not exist!')
    var_context = {
        'var_post': var_foundpost, #my_project/blog/data.py
        'var_title': var_foundpost['title'] + ' - '
    }
    return render(request, 'blog/post.html', context=var_context)

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

{#my_project/blog/templates/blog/post.html:#}

{% extends 'global/base.html' %} {#my_project/base/global/base.html#}
{% block text %} {{key_text}} {% endblock text %} {#my_project/blog/views.py#}

{% block posts %}
    <article class="post single-post"> {#my_project/base/static/global/css/style.css#} {#1:#}
        <header>
            <h1 class="post__title">
                <a href="{% url "blog:blog_post" var_post.id %}"> {#my_project/blog/urls.py#} | {#my_project/blog/data.py#}
                    {{var_post.title}} {#my_project/blog/data.py#}
                </a>
            </h1>
        </header>
        <div class="post__body">
            {{var_post.body}} {#my_project/blog/data.py#}
        </div>
    </article>
{% endblock posts %}

{#my_project/base/global/base.html#}

{% include 'global/partials/head.html' %} {#my_project/base/global/partials/head.html#}
{% include 'global/partials/menu.html' %} {#my_project/base/global/partials/menu.html#}

{% if key_text %} {#my_project/blog/views.py#}
    <h1>{% block text %}{% endblock text %}</h1>
{% endif %}

<main class="content"> {#my_project/base/static/global/css/style.css#}
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
    <title> {{ var_title }} Site do Edsu</title> {#my_project/blog/views.py#}
    <link rel="stylesheet" href="{% static 'global/css/style.css' %}"> {#my_project/base/static/global/css/style.css#}
</head>
<body>
    <h1>Mensagem do HEAD.HTML</h1>

    /* #my_project/base/static/global/css/style.css: */

/* Reset */
*,
*:after,
*:before {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-size: 62.5%;
}

body {
  font-size: 1.6rem;
  background: yellowgreen;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
    Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}

.content {
  display: grid;
  gap: 1.5rem;
  padding: 1.5rem;
}

.post {
  background: yellow;
  padding: 1.5rem;
  box-shadow: 5px 2px 5px rgba(0, 0, 0, 90%);
}

@media (min-width: 600px) {
  .content { /* # -> my_project/base/global/base.html */
    grid-template-columns: repeat(auto-fill, minmax(32rem, 1fr));
  }

}

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
