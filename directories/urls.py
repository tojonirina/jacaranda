from django.urls import path
from .views import DirectoryView

app_name = 'directories'

urlpatterns = [
    path('', DirectoryView.index, name='directory_home'),
    path('store', DirectoryView.store, name='store_directory'),
    path('<int:id>', DirectoryView.show, name='show_directory'),
    path('<int:id>/edit', DirectoryView.edit, name='edit_directory'),
    path('<int:id>/update', DirectoryView.update, name='update_directory'),
    path('<int:id>/delete', DirectoryView.delete, name='delete_directory')
]