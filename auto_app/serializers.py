from rest_framework import serializers
from .models import Car
from .models import Owner

class OwnerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()


class CarSerializer(serializers.Serializer):
    owner = OwnerSerializer()
    brand = serializers.CharField(max_length=44)
    model = serializers.CharField(max_length=50)
    year = serializers.IntegerField()
    
    engine_type = serializers.ChoiceField(choices=[
        ("petrol", "Бензин"),
        ("diesel", "Дизель"),
        ("hybrid", "Гибрид"),
        ("electric", "Электро"),
    ])
    engine_volume = serializers.DecimalField(max_digits=4, decimal_places=1)
    horsepower = serializers.IntegerField()
    torque = serializers.IntegerField(help_text="Ньютон-метры")
    
    transmission = serializers.ChoiceField(choices=[
        ("manual", "Механика"),
        ("automatic", "Автомат"),
        ("cvt", "Вариатор"),
        ("dct", "Робот"),
    ])
    drive_type = serializers.ChoiceField(choices=[
        ("fwd", "Передний"),
        ("rwd", "Задний"),
        ("awd", "Полный"),
    ])
    
    length = serializers.IntegerField(help_text="мм")
    width = serializers.IntegerField(help_text="мм")
    height = serializers.IntegerField(help_text="мм")
    wheelbase = serializers.IntegerField(help_text="мм")
    weight = serializers.IntegerField(help_text="кг")
    
    acceleration_0_100 = serializers.DecimalField(max_digits=4, decimal_places=2, help_text="секунды")
    max_speed = serializers.IntegerField(help_text="км/ч")
    fuel_consumption = serializers.DecimalField(max_digits=4, decimal_places=1, help_text="л/100км")
    safety_rating = serializers.DecimalField(max_digits=3, decimal_places=1, help_text="Оценка безопасности")

    def create(self, validated_data):
        owner_data = validated_data.pop('owner')
        owner = Owner.objects.create(**owner_data)
        car = Car.objects.create(owner=owner, **validated_data)
        return car
    
    def update(self, instance, validated_data):
        owner_data = validated_data.pop('owner')
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        for attr, value in owner_data.items():
            setattr(instance.owner, attr, value)
        instance.owner.save()
        
        return instance