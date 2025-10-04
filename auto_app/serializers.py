from rest_framework import serializers
from .models import Car, Owner, Brand, Color
from django.core.validators import MinValueValidator, MaxValueValidator


class Color(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


    def create(self, validated_data):
        return Color.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance,attr,value)
        instance.save()
        return instance

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"

    def create(self, validated_data):
        return Brand.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['__all__']

    def create(self, validated_data):
        return Owner.objects.create(**validated_data)   
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class CarSerializer(serializers.Serializer):
    class Meta:
        model = Car
        fields = ['__all__']
    
    def create(self, validated_data):
        owner_data = validated_data.pop('owner')
        owner = Owner.objects.create(**owner_data)
        car = Car.objects.create(owner=owner, **validated_data)
        return car
    
    def update(self, instance, validated_data):
        owner_data = validated_data.pop("owner", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if owner_data:
            for attr, value in owner_data.items():
                setattr(instance.owner, attr, value)
            instance.owner.save()

        return instance