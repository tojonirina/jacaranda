def currentUserInfo(request):


    if request.session.get('current_user_id') is not None and request.session.get('current_user_login') is not None and request.session.get('current_user_type') is not None:
        
        current_user_id = request.session.get('current_user_id')
        current_user_login = request.session.get('current_user_login')
        current_user_type = request.session.get('current_user_type')
        current_user_initial = current_user_login[0]
        
    else:
        current_user_id = 0
        current_user_login = None
        current_user_type = None
        current_user_initial = None
        

    return {'current_user_login':current_user_login, 'current_user_type': current_user_type, 'current_user_initial':current_user_initial}