# from django.shortcuts import render
from rest_framework.response import Response
from .models import Product
from .views import ProductSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class ProductDetail('generics'.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    permission_classes = [IsAuthenticated]
    
    def perform_update(self, serializer):
        isinstance = self.get.object()
        quantity = self.request.data.get('quantity',isinstance.quatity)
        if quantity > isinstance.quantity:
            return Response({'error': 'No hay suficiente stock para este producto'}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
