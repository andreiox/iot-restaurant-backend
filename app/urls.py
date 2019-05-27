from django.conf.urls import url
from rest_framework import routers

from app.views import ClientViewSet, TransactionViewSet, CustomView

router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    url(r'customview', CustomView.as_view()),
]

urlpatterns += router.urls
