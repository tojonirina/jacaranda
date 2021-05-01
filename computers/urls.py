from django.urls import path
from .views import ComputerView

app_name = 'computers'

urlpatterns = [
    path('', ComputerView.index, name="computer_home"),
    path('store', ComputerView.store, name="store_computer"),
    path('<int:id>', ComputerView.show, name="show_computer"),
    path('<int:id>/edit', ComputerView.edit, name="edit_computer"),
    path('<int:id>/update', ComputerView.update, name="update_computer"),
]