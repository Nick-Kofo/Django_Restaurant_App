from django.contrib.auth.models import User
from .models import Dish
from rest_framework import serializers


class DishSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Dish
        fields = ('name', 'price', 'type', 'categoryA', 'categoryB', 'photo', 'description', 'pk', 'author')

    def create(self, validated_data):
        return Dish.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.type = validated_data.get('type', instance.type)
        instance.categoryA = validated_data.get('categoryA', instance.categoryA)
        instance.categoryB = validated_data.get('categoryB', instance.categoryB)


class UserSerializer(serializers.ModelSerializer):
    dishes = serializers.PrimaryKeyRelatedField(many=True, queryset=Dish.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'dishes')
