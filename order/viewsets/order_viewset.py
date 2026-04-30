from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
    TokenAuthentication,
)
from rest_framework.permissions import IsAuthenticated, AllowAny

from order.models import Order
from order.serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    authentication_classes = [
        SessionAuthentication,
        BasicAuthentication,
        TokenAuthentication,
    ]
    permission_classes = [AllowAny]
    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by("id")
    pagination_class = None

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
