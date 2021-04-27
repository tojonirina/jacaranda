from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.utils.html import escape
from .models import User
from directories.models import Directories

class UserView:
    
    def index(request):
        """
        Display all user
        """
        try:
            directories = Directories.objects.all()
            # display 10 last user order by its creation date
            users = User.objects.raw('SELECT * FROM users u INNER JOIN directories d ON u.directory_id = d.id ORDER BY u.created_at DESC')[:10]
        except Directorie.DoesNotExist:
            return HttpResponse('Directorie does not exist or database connection error', status=500)
        except User.DoesNotExist:
            return HttpResponse('User does not exist or database connection error', status=500)
        
        return render(request, 'user/home.html', {'users':users, 'directories':directories})

    def store(request):
        """
        Store an user
        """
        try:
            
            if request.method == 'POST':

                if len(request.POST['login']) >= 8:

                    if request.POST['password'] == request.POST['confirm_password']:

                        if request.POST['directory_id'] != None :

                            checkUserID = User.objects.filter(directory_id=int(request.POST['directory_id'])).first()

                            if checkUserID is None:

                                checkUserLogin = User.objects.filter(login=request.POST['login']).first()

                                if checkUserLogin is None:

                                    import hashlib # import haslib for hashing
                                    passwd = bytes(escape(request.POST['confirm_password']), 'ascii') # convert password to bytes for to be readable in sha224() 

                                    user = User()
                                    user.directory_id = request.POST['directory_id']
                                    user.login = escape(request.POST['login'])
                                    user.password = hashlib.sha224(b"%s" % passwd ).hexdigest() # Encrypt password
                                    user.types = request.POST['types']
                                    user.administrator = 'superadmin'
                                    user.save()

                                else :
                                    print('Login already exists')

                            else :
                                print('Already have an account')

                        else :
                            print('You must set full name field')

                    else:
                        print('Error of password')

                else :
                    print("Login lentgh must 8 characters at least")

            else:
                print('Unauthorized')
        except:
            return HttpResponse('Server error', status=500)

        return redirect('users:user_home')

    def show(request, id):
        """
        Show a specific user detail
        """
        try: 
            user = User.objects.raw('SELECT * FROM users u INNER JOIN directories d ON u.directory_id = d.id AND u.id = %s', [id])[0]
        except User.DoesNotExist:
            return HttpResponse('User does not exist or database connection error', status=500)

        return render(request, 'user/show.html', {'user': user})

    def edit(request, id):
        """
        Edit an user information 
        """
        user = get_object_or_404(User, pk=int(id))

        return render(request, 'user/edit.html', {'user': user})

    def update(request, id):
        """
        Update user information
        """
        try:
            if request.method == 'POST':

                user = User.objects.get(id=int(id))

                if user.status != 1:
                    user.types = escape(request.POST['types'])
                    user.save()
                else:
                    print("You're note authorized to change it")

            else:
                return HttpResponse('Unauthorized', status=401)
        except:
            return HttpResponse('Server error', status=500)

        return redirect('users:show_user', id)

    def delete(request, id):
        """
        Delete an user
        """
        try:
            if request.method == 'POST':
                user = User.objects.get(id=id)
                user.delete()
            else:
                return HttpResponse('Unauthorized', status=401)
        except:
            raise Http404('Error')

        return redirect('users:user_home')

    def block(request, id):
        """
        Block user account
        """
        try:
            if request.method == 'POST':
                user = User.objects.get(id=id)
                user.status = 0
                user.save()            
            else:
                return HttpResponse('Unauthorized', status=401)
        except:
            raise Http404('Error')

        return redirect('users:user_home')

    def unblock(request, id):
        """
        Unblock user account
        """
        try:
            if request.method == 'POST':
                user = User.objects.get(id=id)
                user.status = 1
                user.save()
            else:
                return HttpResponse('Unauthorized', status=401)
        except:
            raise Http404('Error')

        return redirect('users:user_home')