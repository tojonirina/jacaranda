from django.http import HttpResponse
from django.shortcuts import render, redirect

def index(request):
    '''
    Get index page or login page
    '''
    if request.session.get('current_user_id') is not None and request.session.get('current_user_login') is not None and request.session.get('current_user_type') is not None :
        return redirect('/users')

    return render(request, 'login.html')

def pageNotFound(request, exception=None):
    return render( request, 'errors/404.html')

def unauthorizedRequest(request, exception=None):
    return HttpResponse('Error 403', status=403)

def serverError(request, exception=None):
    return HttpResponse('Error 500', status=500)