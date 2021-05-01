from django.urls import path
from .views import MaterialView

app_name = 'materials'
urlpatterns = [
    path('', MaterialView.index, name='material_home'),
    path('store', MaterialView.store, name='store_material'),
    path('<int:id>', MaterialView.show, name='show_material'),
    path('<int:id>/edit', MaterialView.edit, name='edit_material'),
    path('<int:id>/update', MaterialView.update, name='update_material'),
    path('takeOut', MaterialView.getTakeOut, name='get_takeout_material'),
    path('takeOut/store', MaterialView.postTakeOut, name='post_takeout_material'),
    path('histories', MaterialView.history, name='history_material'),
    path('reportings', MaterialView.reporting, name='reporting_material'),
]