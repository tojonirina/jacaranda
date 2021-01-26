from django.urls import path
from . import views

app_name = 'material'

urlpatterns = [
    path('', views.home, name='material_home'),
    path('store', views.store, name='store_material'),
    path('<int:id>/edit', views.edit, name='edit_material'),
    path('<int:id>/update', views.update, name='update_material'),
    path('takeOut', views.getTakeOut, name='get_takeout_material'),
    path('takeOut/store', views.postTakeOut, name='post_takeout_material'),
    path('history', views.history, name='history_material'),
]