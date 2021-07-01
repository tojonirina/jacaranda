from django.http import HttpResponse
from django.shortcuts import render, redirect
from users.models import User
from django.contrib import messages

class IndexView:
    
    def index(request):
        '''
        Get index page or login page
        '''
        if request.session.get('current_user_id') is not None and request.session.get('current_user_login') is not None and request.session.get('current_user_type') is not None :
            return redirect('/users')

        user = User.objects.all()
        
        # Check if no user created, create one by default
        if len(user) == 0:
            try:
                import hashlib
                default_password = 'administrator123'.encode('ascii')
                
                user = User()
                user.directory_id = 0
                user.login = 'administrator'
                user.password = hashlib.sha224(default_password).hexdigest() # Encrypt password
                user.types = 'administrator'
                user.administrator = 'administrator'
                user.save()

                messages.success(request,'Use "administrator" as username and "administrator123" as password,Note: this is a temporary access')
            except:
                return HttpResponse('Server or database error')   

        # Check if there is another users, disable the default user
        if len(user) > 1:

            try:
                user = User.objects.get(directory_id=0)
                user.status = 0
                user.save()
            except:
                return HttpResponse('Server or database error')      

        return render(request, 'login.html')