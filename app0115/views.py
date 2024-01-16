from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


# views for webpage notes 0115
def home(request):
    return render(request, '0115_homepage_links.html', {})
def token_home(request):
    return render(request, '0115_django_token_auth_demo1.html', {})
def debug_install(request):
    return render(request, '0115_django_debug_install_demo2.html', {})
def git_install(request):
    return render(request, '0115_git_install_notes.html', {})


# ex0115 add secret api for permission access only
@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({"message": "insert secret txt @011524' @2042"})
