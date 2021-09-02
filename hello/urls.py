from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact")
]

# Be mindful that the name argument to the path function defines the name with which
# you refer to the page in the { % url % } tags in the templates in templates/hello/layout.html lines 13-15
