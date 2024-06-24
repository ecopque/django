#my_project/project/settings.py:
STATIC_URL = 'static/' #1:

#my_project/home/templates/home/index.html: #2:
{% extends 'global/base.html' %}

#my_project/base/global/base.html: #3:
<body>
    <h1>{% block text %} BASE 01 {% endblock text %}</h1>
</body>
{% include 'global/partials/head.html' %}
</html>

#my_project/home/static/home/css/blue.css: #4:
body {
    background: blue;
}

#my_project/base/global/partials/head.html:
{% load static %} <!DOCTYPE html> #5:
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Include Worked</title>
    <link rel="stylesheet" href="{% static 'home/css/blue.css' %}"> #6:
</head>
<body>
    <h1>Aaaaaaaah</h1>
