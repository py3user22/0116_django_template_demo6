from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


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

    # secret api demo0115
    path('secret/', views.secret),
    path('api/secret/', views.secret),
    path('api-token-auth/', obtain_auth_token),
    path('manager-view/', views.manager_view),
]

""" demo5 0116
    path('menu-items/', views.menu_items),
    path('menu-items/<int:id>', views.single_item),

    

    path('throttle-check/', views.throttle_check),
    path('throttle-check-auth/', views.throttle_check_auth),

    path('roles/', views.roles),
    path('me/', views.me),
    
"""

