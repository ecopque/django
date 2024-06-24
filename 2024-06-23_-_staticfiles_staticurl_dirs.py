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

#my_project/base/static/global/css/red.html: #5: (#9)
body {
    background: red;
}

#my_project/base/global/partials/head.html:
{% load static %} <!DOCTYPE html> #6:
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Include Worked</title>
    <link rel="stylesheet" href="{% static 'home/css/blue.css' %}"> #7:
    <link rel="stylesheet" href="{% static 'global/css/red.css' %}"> #8: (#5) (#9)
</head>
<body>
    <h1>Aaaaaaaah</h1>

#my_project/project/settings.py: #9:
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'base' / 'static'
]
