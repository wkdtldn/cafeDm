from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
