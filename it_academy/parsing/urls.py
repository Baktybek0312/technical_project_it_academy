from django.urls import path

from .views import *

urlpatterns = [
    path('', InfoViewSet.as_view({'get': 'list'}), name='pars_data'),
]
