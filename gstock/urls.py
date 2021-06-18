from django.urls import path, include
from .views import IndexView

urlpatterns = [
    path('', IndexView.index, name='login_page'),
    path('index/', IndexView.index, name='index_page'),
    path('default/', IndexView.index, name='default_page'),
    path('users/', include('users.urls')),
    path('materials/', include('materials.urls')),
    path('directories/', include('directories.urls')),
    path('computers/', include('computers.urls')),
    path('absences/', include('absences.urls'))
]
