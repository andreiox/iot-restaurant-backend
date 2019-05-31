from django.db import models


class Client(models.Model):
    cpf = models.CharField(max_length=255, unique=True)
    rfid = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __unicode__(self):
        return self.name


class Transaction(models.Model):
    date = models.DateTimeField()
    value = models.DecimalField(max_digits=8, decimal_places=2)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'
