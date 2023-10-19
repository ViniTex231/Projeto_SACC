from rest_framework import viewsets
from App_SAC.API import serializers
from App_SAC import models
#from django.filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


#from rest_framework.permissions import isAuthenticated

class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ClienteSerializer
    queryset = models.Cliente.objects.all()
    #filter_backends = [DjangoFilterBackEnd]
    #filterset_fields = ['nome', 'telefone', 'email']

    filter_backends = [filters.SearchFilter]
    search_fields = ['nome', 'telefone', 'email', 'observacao']

class AtendimentoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AtendimentoSerializer
    queryset = models.Atendimento.objects.all()
    #permission_classes = (IsAuthenticated,)
    #filter_backends = [DjangoFilterBackend]
    filter_backends = [filters.SearchFilter]
    search_fields = ['cliente_nome', 'cliente__telefone', 'cliente__email', 'cliente__observacao', 'solicitacao']