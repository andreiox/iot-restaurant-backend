from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView, Response
from rest_framework.pagination import PageNumberPagination

from .models import Client
from .models import Transaction
from .serializers import ClientSerializer
from .serializers import TransactionSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        queryset = Client.objects.all().order_by('id')

        rfid = self.request.query_params.get('rfid', None)
        if rfid is not None:
            queryset = queryset.filter(rfid=rfid)

        return queryset


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        queryset = Transaction.objects.all().order_by('id')

        client_id = self.request.query_params.get('client_id', None)
        if client_id is not None:
            queryset = queryset.filter(client_id=client_id)

        return queryset


class CustomView(APIView):
    def get(self, request, format=None):
        return Response("Some Get Response")

    def post(self, request, format=None):
        return Response("Some Post Response")
