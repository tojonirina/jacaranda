from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.utils.html import escape
from django.contrib import messages
from .models import User, SessionHistory
from directories.models import Directory

class UserView:

    # Post login
    def login(request):

        try:

            if request.method == 'POST':
                    
                import hashlib # import haslib to hash the password

                login = request.POST['login']

                # cast password to a byte
                password = bytes(escape(request.POST['password']), 'ascii')

                # encrypt password
                crypted_password = hashlib.sha224(b"%s" % password ).hexdigest()

                # check login and password
                user = User.objects.get(login=login, password=crypted_password)

                # Check if the account is not blocked
                if user.status == 1:

                    request.session['current_user_id'] = user.id
                    request.session['current_user_login'] = user.login
                    request.session['current_user_type'] = user.types
                    request.session['current_user_ua'] = request.headers['user-agent']

                    import os 
                    import platform

                    newSession = SessionHistory()
                    newSession.user_id = user.id
                    newSession.login = user.login
                    newSession.user_agent = request.headers['user-agent']
                    newSession.computer_user = os.getlogin()
                    newSession.computer_name = platform.uname()[1]
                    newSession.save()

                    if user.types == 'user':
                        return redirect('directories:directory_home')
                    elif user.types == 'administrator' or user.types == 'super_user':
                        return redirect('users:user_home')
                    else:
                        return redirect('login_page')

                else:
                    messages.error(request, 'This account is blocked, please contact your administrator')
                    return redirect('login_page')

            else:
                return HttpResponse('You are not authorized', status=403)

        except User.DoesNotExist:
            messages.error(request, 'Login or password invalid')
            return redirect('login_page')

    # Logout 
    def logout(request):

        if request.method == 'POST':
            
            # Disconnect all session of the current user in the same browser, computer
            mysession = SessionHistory.objects.get(login=request.session.get('current_user_login'), user_id=int(request.session.get('current_user_id')), logged=True, user_agent=request.session.get('current_user_ua'))
            mysession.logged = False
            mysession.save()

            # Remove all session
            request.session.flush()
            messages.success(request, 'You are disconnected')
            return redirect('login_page')

        else:
            return HttpResponse('You are not authorized', status=403)
            
    # Display all user
    def index(request):

        # Check if connected
        if request.session.get('current_user_login') is None and request.session.get('current_user_id') is None and request.session.get('current_user_type') is None :
            messages.error(request, 'Sorry, you are not connected, if you do not have an account please contact an administrator')
            return redirect('login_page')

        # Check if the user is an simple user or other, only admin or super user can access this page
        if request.session.get('current_user_type') != 'administrator':
            if request.session.get('current_user_type') != 'super_user':
                messages.error(request, 'Sorry, you are not able to visit this resource')
                return redirect('directories:directory_home')
        
        try:
            # Select all directory whose not have an account
            directories = Directory.objects.raw('SELECT d.full_name, d.id , u.directory_id FROM directories d LEFT JOIN users u ON d.id == u.directory_id WHERE u.directory_id IS NULL')
            # directories = Directory.objects.raw('SELECT full_name, id FROM directories  WHERE id NOT IN (SELECT directory_id FROM users)')
            
            # display 10 last user order by its creation date
            users = User.objects.raw('SELECT d.full_name, u.id, u.login, u.types, u.status, u.administrator, u.created_at, u.updated_at FROM users u INNER JOIN directories d ON u.directory_id = d.id ORDER BY u.created_at DESC')
        except Directory.DoesNotExist:
            return HttpResponse('Directorie does not exist or database connection error', status=500)
        except User.DoesNotExist:
            return HttpResponse('User does not exist or database connection error', status=500)
        finally:
            return render(request, 'user/home.html', {'users':users, 'directories':directories})

    # Store a new user
    def store(request):
        # Check if connected
        if request.session.get('current_user_login') is None and request.session.get('current_user_id') is None and request.session.get('current_user_type') is None :
            messages.error(request, 'Sorry, you are not connected, if you do not have an account please contact an administrator')
            return redirect('login_page')
        
        # Check if the user is an simple user or other, only admin or super user can access this page
        if request.session.get('current_user_type') != 'administrator':
            if request.session.get('current_user_type') != 'super_user':
                messages.error(request, 'Sorry, you are not able to visit this resource')
                return redirect('directories:directory_home')

        try:
            
            if request.method == 'POST':

                # Check login if it contains a special char or not
                import re
                checkCharInLogin = re.search("[()\-\_\\|=+#@!*&%$ ~?{}/<>:;\'\"\[\]]", request.POST['login'])
                
                if len(request.POST['login']) >= 8 and checkCharInLogin is None:

                    if request.POST['password'] == request.POST['confirm_password']:

                        if request.POST['directory_id'] != None :

                            checkUserID = User.objects.filter(directory_id=int(request.POST['directory_id'])).first()

                            if checkUserID is None:

                                checkUserLogin = User.objects.filter(login=request.POST['login']).first()

                                if checkUserLogin is None:

                                    import hashlib # import haslib to hash the password
                                    password = bytes(escape(request.POST['confirm_password']), 'ascii') # convert password to bytes for to be readable in sha224() and escape all special char 

                                    user = User()
                                    user.directory_id = request.POST['directory_id']
                                    user.login = escape(request.POST['login'])
                                    user.password = hashlib.sha224(b"%s" % password ).hexdigest() # Encrypt password
                                    user.types = request.POST['types']
                                    user.administrator = request.session.get('current_user_login')
                                    user.save()

                                    messages.success(request,'User added successfully')

                                else :
                                    messages.error(request, 'Login already exists')

                            else :
                                messages.error(request, 'Already have an account')

                        else :
                            messages.error(request, 'You must set full name field')

                    else:
                        messages.error(request, 'Two password must same')

                else :
                    messages.warning(request, "Login lentgh must 8 characters at least and don't contains special char except a dot")

            else:
                return HttpResponse('Forbidden request', status=403)
        except:
            return HttpResponse('Server error', status=500)

        return redirect('users:user_home')

    # Show a specific user detail
    def show(request, id):

        # Check if connected
        if request.session.get('current_user_login') is None and request.session.get('current_user_id') is None and request.session.get('current_user_type') is None :
            messages.error(request, 'Sorry, you are not connected, if you do not have an account please contact an administrator')
            return redirect('login_page')

        # Check if the user is an simple user or other, only admin or super user can access this page
        if request.session.get('current_user_type') != 'administrator':
            if request.session.get('current_user_type') != 'super_user':
                messages.error(request, 'Sorry, you are not able to visit this resource')
                return redirect('directories:directory_home')

        try: 
            user = User.objects.raw('SELECT d.full_name, u.id, u.login, u.types, u.status, u.administrator, u.created_at, u.updated_at FROM users u INNER JOIN directories d ON u.directory_id = d.id AND u.id = %s', [id])[0]
        except:
            return HttpResponse('User does not exist or database connection error', status=500)

        return render(request, 'user/show.html', {'user': user})

    # Edit an user information
    def edit(request, id):
       
       # Check if connected
        if request.session.get('current_user_login') is None and request.session.get('current_user_id') is None and request.session.get('current_user_type') is None :
            messages.error(request, 'Sorry, you are not connected, if you do not have an account please contact an administrator')
            return redirect('login_page')

        # Check if the user is an simple user or other, only admin or super user can access this page
        if request.session.get('current_user_type') != 'administrator':
            if request.session.get('current_user_type') != 'super_user':
                messages.error(request, 'Sorry, you are not able to visit this resource')
                return redirect('directories:directory_home')

        try: 
            user = User.objects.raw('SELECT d.full_name, u.id, u.login, u.types, u.directory_id FROM users u INNER JOIN directories d ON u.directory_id = d.id AND u.id = %s', [id])[0]
        except:
            return HttpResponse('User does not exist or database connection error', status=500)

        return render(request, 'user/edit.html', {'user': user})
    
    # Update user information
    def update(request, id):

        # Check if connected
        if request.session.get('current_user_login') is None and request.session.get('current_user_id') is None and request.session.get('current_user_type') is None :
            messages.error(request, 'Sorry, you are not connected, if you do not have an account please contact an administrator')
            return redirect('login_page')

        # Check if the user is an simple user or other, only admin or super user can access this page
        if request.session.get('current_user_type') != 'administrator':
            if request.session.get('current_user_type') != 'super_user':
                messages.error(request, 'Sorry, you are not able to visit this resource')
                return redirect('directories:directory_home')

        try:
            if request.method == 'POST':

                user = User.objects.filter(id=int(id)).first()

                # Check if the user is actif
                if user.status == 1:

                    user.types = escape(request.POST['types'])
                    user.save()

                    messages.success(request,'User updated successfully')

                else:
                    messages.warning(request, "This user cannot be edited")

            else:
                return HttpResponse('Forbidden request', status=403)
        except:
            return HttpResponse('Server or DB error', status=500)

        return redirect('users:show_user', id)

    # Delete an user
    def delete(request, id):

        # Check if connected
        if request.session.get('current_user_login') is None and request.session.get('current_user_id') is None and request.session.get('current_user_type') is None :
            messages.error(request, 'Sorry, you are not connected, if you do not have an account please contact an administrator')
            return redirect('login_page')

        # Check if the user is an simple user or other, only admin or super user can access this page
        if request.session.get('current_user_type') != 'administrator':
            if request.session.get('current_user_type') != 'super_user':
                messages.error(request, 'Sorry, you are not able to visit this resource')
                return redirect('directories:directory_home')

        try:
            if request.method == 'POST':

                user = User.objects.get(id=id)
                user.delete()

                messages.success(request,'User deteled successfully')

            else:
                return HttpResponse('Forbidden request', status=403)
        except User.DoesNotExist:
            return HttpResponse('Server or DB error', status=500)

        return redirect('users:user_home')

    # Block user account
    def block(request, id):

        # Check if connected
        if request.session.get('current_user_login') is None and request.session.get('current_user_id') is None and request.session.get('current_user_type') is None :
            messages.error(request, 'Sorry, you are not connected, if you do not have an account please contact an administrator')
            return redirect('login_page')

        # Check if the user is an simple user or other, only admin or super user can access this page
        if request.session.get('current_user_type') != 'administrator':
            if request.session.get('current_user_type') != 'super_user':
                messages.error(request, 'Sorry, you are not able to visit this resource')
                return redirect('directories:directory_home')

        try:
            if request.method == 'POST':
                user = User.objects.get(id=id)
                # Check if not the current user
                if request.session.get('current_user_id') != int(id):
                    # Check if the user is admin or super user
                    if request.session.get('current_user_type') == 'administrator' or request.session.get('current_user_type') == 'super_user':
                        user.status = 0
                        user.save()
                        messages.warning(request,'User blocked')
                    else:
                        messages.error(request,'You are not able to block this user')
                else:
                    messages.error(request,'You can\'t block this user')
            else:
                return HttpResponse('Forbidden request', status=403)
        except User.DoesNotExist:
            return HttpResponse('Server or DB error', status=500)

        return redirect('users:user_home')

    # Unblock user account
    def unblock(request, id):

        # Check if connected
        if request.session.get('current_user_login') is None and request.session.get('current_user_id') is None and request.session.get('current_user_type') is None :
            messages.error(request, 'Sorry, you are not connected, if you do not have an account please contact an administrator')
            return redirect('login_page')

        # Check if the user is an simple user or other, only admin or super user can access this page
        if request.session.get('current_user_type') != 'administrator':
            if request.session.get('current_user_type') != 'super_user':
                messages.error(request, 'Sorry, you are not able to visit this resource')
                return redirect('directories:directory_home')

        try:
            if request.method == 'POST':
                user = User.objects.get(id=int(id))
                user.status = 1
                user.save()
                messages.success(request,'User unlocked successfully')
            else:
                return HttpResponse('Forbidden request', status=403)
        except User.DoesNotExist:
            return HttpResponse('Server or DB error', status=500)

        return redirect('users:user_home')

    # Get all session history
    def history(request):

        try:
            sessions = SessionHistory.objects.all()
        except:
            return HttpResponse('Server or database error', status=500)

        return render(request, 'user/history.html', {'sessions':sessions})