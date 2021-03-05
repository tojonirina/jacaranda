from django.urls import path
from . import views

app_name = 'directories'

urlpatterns = [
    path('', views.home, name='directory_home'),
    path('store', views.store, name='store_directory'),
    path('<int:id>', views.show, name='show_directory'),
    path('<int:id>/edit', views.edit, name='edit_directory'),
    path('<int:id>/update', views.update, name='update_directory'),
    path('<int:id>/delete', views.delete, name='delete_directory')
]