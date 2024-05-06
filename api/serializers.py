from rest_framework import serializers
from cakeoperations.models import *

class UserSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields="__all__"

    # def create(self,validated_data):
    #     return User.objects.create_user(**validated_data)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"

class CakeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cakes
        fields="__all__"

class CakeVarientSerializer(serializers.ModelSerializer):
    class Meta:
        model=CakeVarients
        fields="__all__"

class OfferCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Offer
        exclude="cakevarient"