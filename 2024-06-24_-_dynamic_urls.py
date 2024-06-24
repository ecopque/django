#my_project/base/global/partials/menu.html:
<nav> #1:
    <ul> #2:
        <li> #3:
            <a href="{% url 'home' %}">Home</a> #4:
        </li>
        <li>
            <a href="{% url 'blog' %}">Blog</a>
        </li>
        <li>
            <a href="{% url 'example' %}">Example</a>
        </li>
    </ul>
</nav>

#my_project/base/global/base.html:
{% include 'global/partials/menu.html' %} #5:
<body>
    <h1>{% block text %} BASE 01 {% endblock text %}</h1> #6:
</body>
{% include 'global/partials/head.html' %} #7:
</html>

#my_project/home/urls.py:
from django.urls import path
from home import views as home_views
urlpatterns = [
    path('', home_views.func_home, name='home'), #8:
]

#my_project/blog/urls.py:
from django.urls import path
from blog import views as blog_views
urlpatterns = [
    path('', blog_views.func_blog, name='blog'),
    path('example', blog_views.func_example, name='example')
]
