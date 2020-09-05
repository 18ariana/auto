from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Order, Status
from .serializers import OrderCreateSerializer, OrderListSerializer, OrderDetailSerializer, OrderUpdateSerializer, OrderStatusSerializer
from django.db.models import F, FloatField, ExpressionWrapper, Func
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

class Round(Func):
    function = 'ROUND'
    arity = 2


class OrderListView(generics.ListAPIView):
    """Вывод заказов"""

    def get_queryset(self):
        order = Order.objects.all().annotate(
            total_cost=ExpressionWrapper(Round(F("amount_actual") * F("cost"), 2), output_field=FloatField())).order_by('status')
        return order

    serializer_class = OrderListSerializer


class OrderAddView(generics.CreateAPIView):
    """Добавление заказа"""
    serializer_class = OrderCreateSerializer
    permission_class = permissions.IsAuthenticated


class OrderViewset(viewsets.ModelViewSet):
    """Удаление заказа"""
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_class = permissions.IsAuthenticated


class OrderPartialUpdateView(generics.UpdateAPIView):
    """Обновление статуса заказа"""
    queryset = Order.objects.all()
    serializer_class = OrderUpdateSerializer
    permission_class = permissions.IsAuthenticated


class OrderDetailView(generics.RetrieveAPIView):
    """Вывод 1 заказа"""
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer


class Logout(APIView):

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class StatusView(generics.ListAPIView):
    queryset = Status.objects.all()
    serializer_class = OrderStatusSerializer
