from django.contrib import admin
from .models import Client
from .models import Transaction

admin.site.register(Client)
admin.site.register(Transaction)
