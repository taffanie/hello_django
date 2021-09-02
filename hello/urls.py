from django.urls import path
from hello import views
from hello.models import LogMessage

home_list_view = views.HomeListView.as_view(
    # :5 limits the results to the five most recent
    queryset=LogMessage.objects.order_by("-log_date")[:5],
    context_object_name="message_list",
    template_name="hello/home.html",
)

urlpatterns = [
    # path("", views.home, name="home"),
    path("", home_list_view, name="home"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("log/", views.log_message, name="log")
]

# Be mindful that the name argument to the path function defines the name with which
# you refer to the page in the { % url % } tags in the templates in templates/hello/layout.html lines 13-15
