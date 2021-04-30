from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.utils.html import escape
from django.contrib import messages
from .models import User
from directories.models import Directory
import re

class UserView:
    
    # Display all user
    def index(request):
        try:
            # Select all directory whose not have an account
            directories = Directory.objects.raw('SELECT full_name, id FROM directories  WHERE id NOT IN (SELECT directory_id FROM users)')
            # display 10 last user order by its creation date
            users = User.objects.raw('SELECT d.full_name, u.id, u.login, u.types, u.status, u.administrator, u.created_at, u.updated_at FROM users u INNER JOIN directories d ON u.directory_id = d.id ORDER BY u.created_at DESC')
        except Directory.DoesNotExist:
            return HttpResponse('Directorie does not exist or database connection error', status=500)
        except User.DoesNotExist:
            return HttpResponse('User does not exist or database connection error', status=500)
        
        return render(request, 'user/home.html', {'users':users, 'directories':directories})

    # Store a new user
    def store(request):
        try:
            
            if request.method == 'POST':

                # Check login if it contains a special char or not
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
                                    user.administrator = 'superadmin'
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
        try: 
            user = User.objects.raw('SELECT d.full_name, u.id, u.login, u.types, u.status, u.administrator, u.created_at, u.updated_at FROM users u INNER JOIN directories d ON u.directory_id = d.id AND u.id = %s', [id])[0]
        except:
            return HttpResponse('User does not exist or database connection error', status=500)

        return render(request, 'user/show.html', {'user': user})

    # Edit an user information
    def edit(request, id):
        try: 
            user = User.objects.raw('SELECT d.full_name, u.id, u.login, u.types, u.directory_id FROM users u INNER JOIN directories d ON u.directory_id = d.id AND u.id = %s', [id])[0]
        except:
            return HttpResponse('User does not exist or database connection error', status=500)

        return render(request, 'user/edit.html', {'user': user})
    
    # Update user information
    def update(request, id):
        try:
            if request.method == 'POST':

                user = User.objects.get(id=int(id))

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
        try:
            if request.method == 'POST':
                user = User.objects.get(id=id)
                user.status = 0
                user.save()
                
                messages.error(request,'User blocked')
            else:
                return HttpResponse('Forbidden request', status=403)
        except User.DoesNotExist:
            return HttpResponse('Server or DB error', status=500)

        return redirect('users:user_home')

    # Unblock user account
    def unblock(request, id):
        try:
            if request.method == 'POST':
                
                user = User.objects.get(id=id)
                user.status = 1
                user.save()

                messages.success(request,'User unlocked successfully')  
            else:
                return HttpResponse('Forbidden request', status=403)
        except User.DoesNotExist:
            return HttpResponse('Server or DB error', status=500)

        return redirect('users:user_home')
