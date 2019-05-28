import json
import decimal
import datetime

from django.utils import timezone
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
        queryset = Transaction.objects.all().order_by('-id')

        client_id = self.request.query_params.get('client_id', None)
        if client_id is not None:
            queryset = queryset.filter(client_id=client_id)

        return queryset


class MakeTransactionView(APIView):
    def post(self, request, format=None):
        body = json.loads(request.body)

        value = body['value']
        date = datetime.datetime.now(tz=timezone.utc)
        client = Client.objects.get(pk=body['client_id'])

        t = Transaction(date=date, value=body['value'], client=client)
        t.save()

        client.balance += decimal.Decimal(body['value'])
        client.save()

        return Response(TransactionSerializer(t).data)
