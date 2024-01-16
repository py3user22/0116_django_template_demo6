from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('home', views.home),
    path('0115_homepage_links.html', views.home),

    path('git_notes', views.git_install),
    path('0115_git_install_notes.html', views.git_install),

    path('token_notes', views.token_home),
    path('0115_django_token_auth_demo1.html', views.token_home),

    path('django_debug', views.debug_install),
    path('0115_django_debug_install_demo2.html', views.debug_install),
]
