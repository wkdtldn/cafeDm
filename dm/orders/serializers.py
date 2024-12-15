from rest_framework import serializers
from .models import Order, Drink


class DrinkOptionsSerializer(serializers.Serializer):
    ice = serializers.IntegerField(required=False, min_value=0)
    hot = serializers.IntegerField(required=False, min_value=0)


class DrinkSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    options = serializers.JSONField()


class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    drinks = serializers.ListField(
        child=serializers.DictField(child=serializers.JSONField())
    )
    order_by = serializers.ChoiceField(choices=["현금", "송금", "쿠폰"])

    class Meta:
        model = Order
        fields = ["drinks", "order_by"]

    def create(self, validated_data):
        drinks_list = validated_data.pop("drinks")

        order = Order.objects.create(**validated_data)

        for drink_data in drinks_list:
            print(drink_data)
            for drink_name, drink_options in drink_data.items():
                if drink_options:
                    Drink.objects.create(
                        order=order,
                        name=drink_name,
                        ice=drink_options["ice"],
                        hot=drink_options["hot"],
                    )
                else:
                    Drink.objects.create(
                        order=order,
                        name=drink_name,
                    )

        return order
