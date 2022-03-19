from django.urls import path

from .views import *

urlpatterns = [
    path('', TestViewSet.as_view({'get': 'list'}), name='pars_data'),
    # path('', TestViewSet(), name='pars_data'),
]
