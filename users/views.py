from django.http.response import Http404, HttpResponse
from django.shortcuts import redirect, render
from .models import Users
from directories.models import Directories

def home(request):
    """
    Display all user
    """
    try:
        directories = Directories.objects.raw('SELECT * FROM directories')
        users = Users.objects.raw('SELECT * FROM users u INNER JOIN directories d ON u.directory_id = d.id')
    except:
        return HttpResponse('Server error', status=500)

    return render(request, 'user/home.html', {'users':users, 'directories':directories})

def store(request):
    """
    Store an user
    """
    try:

        if request.method == 'POST':

            if request.POST['password'] == request.POST['confirm_password']:

                user = Users()
                user.directory_id = request.POST['directory_id']
                user.login = request.POST['login']
                user.password = request.POST['confirm_password']
                user.types = request.POST['types']
                user.administrator = 'superadmin'
                user.status = 1
                user.save()

            else:
                return Http404('Error of password')

        else:
            return HttpResponse('Unauthorized', status=401)
    except:
        return HttpResponse('Server error', status=500)

    return redirect('users:user_home')

def show(request, id):
    """
    Show a specific user detail
    """
    try: 
        user = Users.objects.raw('SELECT * FROM users u INNER JOIN directories d ON u.directory_id = d.id AND u.id = %s', [id])[0]
    except:
        return HttpResponse('Server error', status=500)

    return render(request, 'user/show.html', {'user': user})

def edit(request, id):
    """
    Edit an user information 
    """
    try: 
        user = Users.objects.raw('SELECT * FROM users u INNER JOIN directories d ON u.directory_id = d.id AND u.id = %s', [id])[0]
    except:
        return HttpResponse('Server error', status=500)

    return render(request, 'user/edit.html', {'user': user})

def update(request, id):
    """
    Update user information
    """
    try:
        if request.method == 'POST':

            user = Users.objects.get(id=id)
            user.full_name = request.POST['full_name']
            user.login = request.POST['login']
            user.types = request.POST['types']
            user.save()

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
            user = Users.objects.get(id=id)
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
            user = Users.objects.get(id=id)
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
            user = Users.objects.get(id=id)
            user.status = 1
            user.save()
        else:
            return HttpResponse('Unauthorized', status=401)
    except:
        raise Http404('Error')

    return redirect('users:user_home')