from rest_framework import viewsets
from cart.models import Cart
from cart.serializers import CartSerializer, CartCreateSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_serializer_class(self):
        method = self.request.method
        if method == "PUT" or method == "POST":
            return CartCreateSerializer
        else:
            return CartSerializer

