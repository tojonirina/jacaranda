from django.urls import path
from .views import UserView

app_name = 'users'

urlpatterns = [
    path('', UserView.index, name='user_home'),
    path('login', UserView.login, name='post_login_user'),
    path('logout', UserView.logout, name='post_logout_user'),
    path('store', UserView.store, name='store_user'),
    path('<int:id>', UserView.show, name='show_user'),
    path('<int:id>/edit', UserView.edit, name='edit_user'),
    path('<int:id>/update', UserView.update, name='update_user'),
    path('<int:id>/delete', UserView.delete, name='delete_user'),
    path('<int:id>/block', UserView.block, name='block_user'),
    path('<int:id>/unblock', UserView.unblock, name='unblock_user'),
    path('histories', UserView.history, name='history_session'),
]