from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='user_home'),
    path('store', views.store, name='store_user'),
    path('<int:id>/', views.show, name='show_user'),
    path('<int:id>/edit', views.edit, name='edit_user'),
    path('<int:id>/update', views.update, name='update_user'),
    path('<int:id>/delete', views.delete, name='delete_user'),
    path('<int:id>/block', views.block, name='block_user'),
    path('<int:id>/unblock', views.unblock, name='unblock_user'),
]