from rest_framework.response import Response
from rest_framework import viewsets

from .pars import habr_articles
from .models import InfoHabrs
from .serializers import InfoHabrSerializer


class TestViewSet(viewsets.ModelViewSet):
    queryset = InfoHabrs.objects.all()
    serializer_class = InfoHabrSerializer

    def retrieve(self, request, *args, **kwargs):
        data = habr_articles(request)
        for i in range(1, data + 1):
            return Response({'data_list': data})

    def list(self, request, *args, **kwargs):
        data = habr_articles(request)
        for i in range(1, int(str(data)) + 1):
            return Response({'data_list': data})






