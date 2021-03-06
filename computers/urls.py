from django.urls import path
from . import views

app_name = 'computers'

urlpatterns = [
    path('', views.home, name="computer_home"),
    path('store', views.store, name="store_computer"),
    path('<int:id>', views.show, name="show_computer"),
    path('<int:id>/edit', views.edit, name="edit_computer"),
    path('<int:id>/update', views.update, name="update_computer"),
    path('<int:id>/delete', views.delete, name="delete_computer"),
]