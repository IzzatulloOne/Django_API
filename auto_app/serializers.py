from rest_framework import serializers
from .models import Car, Owner, Brand, Color

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer()

    class Meta:
        model = Car
        fields = '__all__'

    def create(self, validated_data):
        owner_data = validated_data.pop('owner', None)
        if owner_data:
            owner = Owner.objects.create(**owner_data)
        else:
            owner = None
        car = Car.objects.create(owner=owner, **validated_data)
        return car

    def update(self, instance, validated_data):
        owner_data = validated_data.pop('owner', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if owner_data:
            if instance.owner:
                for attr, value in owner_data.items():
                    setattr(instance.owner, attr, value)
                instance.owner.save()
            else:
                instance.owner = Owner.objects.create(**owner_data)
                instance.save()

        return instance
