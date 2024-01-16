from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, '0115_homepage_links.html', {})

def token_home(request):
    return render(request, '0115_django_token_auth_demo1.html', {})
def debug_install(request):
    return render(request, '0115_django_debug_install_demo2.html', {})
def git_install(request):
    return render(request, '0115_git_install_notes.html', {})
