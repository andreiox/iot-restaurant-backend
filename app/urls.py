from django.conf.urls import url
from rest_framework import routers

from app.views import ClientViewSet, TransactionViewSet, MakeTransactionView

router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    url(r'make_transaction', MakeTransactionView.as_view()),
]

urlpatterns += router.urls
