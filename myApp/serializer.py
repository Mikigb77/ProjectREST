

from rest_framework import serializers

from myApp.models import Drink


class DrinkSerializer (serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = "__all__"
