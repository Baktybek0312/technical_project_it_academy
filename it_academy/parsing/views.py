from rest_framework.response import Response
from rest_framework import viewsets

from .pars import *
from .models import InfoHabrs
from .serializers import InfoHabrSerializer


class InfoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InfoHabrs.objects.all()
    serializer_class = InfoHabrSerializer

    def retrieve(self, request, *args, **kwargs):
        data = habr_articles(request)
        return Response({'data_list': data})

    def list(self, request, *args, **kwargs):
        data = habr_articles(request)
        return Response({'data_list': data})

