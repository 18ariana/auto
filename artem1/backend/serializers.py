from rest_framework import serializers
from .models import Order, Status


class OrderCreateSerializer(serializers.ModelSerializer):
    """Показ 1 заказа"""

    class Meta:
        model = Order
        fields = "__all__"

    def create(self, validated_data):
        return Order.objects.create(**validated_data)


class OrderListSerializer(serializers.ModelSerializer):
    total_cost = serializers.FloatField()
    term = serializers.DateField()
    term_wanted = serializers.DateField()
    status = serializers.SlugRelatedField(slug_field="status", read_only=True)

    class Meta:
        model = Order
        fields = ("id", "number", "term", "amount_actual", "total_cost", "status", "term_wanted", "description")


class OrderDetailSerializer(serializers.ModelSerializer):
    total_cost = serializers.FloatField()
    status = serializers.SlugRelatedField(slug_field="status", read_only=True)

    class Meta:
        model = Order
        fields = "__all__"


class OrderUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ("status", "id")


class OrderStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = "__all__"
