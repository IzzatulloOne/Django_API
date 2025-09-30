from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Owner(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    sex = models.CharField(max_length=10, choices=[
        ("male", "Мужской"),
        ("female", "Женский"),
        ("other", "Другой"),
    ])

    def __str__(self):
        return self.name


class Car(models.Model):
    # 🚗👤

    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    # 🔧 
    brand = models.CharField(max_length=50)              
    model = models.CharField(max_length=50)              
    year = models.PositiveIntegerField()                 
    
    engine_type = models.CharField(max_length=30, choices=[
        ("petrol", "Бензин"),
        ("diesel", "Дизель"),
        ("hybrid", "Гибрид"),
        ("electric", "Электро"),
    ])
    engine_volume = models.DecimalField(max_digits=4, decimal_places=1)  
    horsepower = models.PositiveIntegerField()           
    torque = models.PositiveIntegerField(help_text="Ньютон-метры")  
    
    transmission = models.CharField(max_length=20, choices=[
        ("manual", "Механика"),
        ("automatic", "Автомат"),
        ("cvt", "Вариатор"),
        ("dct", "Робот"),
    ])
    drive_type = models.CharField(max_length=10, choices=[
        ("fwd", "Передний"),
        ("rwd", "Задний"),
        ("awd", "Полный"),
    ])
    
    # 📏 
    length = models.PositiveIntegerField(help_text="мм")
    width = models.PositiveIntegerField(help_text="мм")
    height = models.PositiveIntegerField(help_text="мм")
    wheelbase = models.PositiveIntegerField(help_text="мм")
    weight = models.PositiveIntegerField(help_text="кг")
    
    # ⚡ 
    acceleration_0_100 = models.DecimalField(max_digits=4, decimal_places=2, help_text="секунды")
    max_speed = models.PositiveIntegerField(help_text="км/ч")
    fuel_consumption = models.DecimalField(max_digits=4, decimal_places=1, help_text="л/100км")
    
    # 🛡 
    safety_rating = models.PositiveSmallIntegerField(help_text="Рейтинг Euro NCAP (0-5 звезд)")
    
    # 🛋 
    seats = models.PositiveSmallIntegerField(default=4)
    has_air_conditioner = models.BooleanField(default=True)
    has_multimedia = models.BooleanField(default=True)
    
    # 🎨 
    body_type = models.CharField(max_length=30, choices=[
        ("sedan", "Седан"),
        ("coupe", "Купе"),
        ("hatchback", "Хэтчбек"),
        ("suv", "Внедорожник"),
        ("roadster", "Родстер"),
        ("pickup", "Пикап"),
    ])
    color = models.CharField(max_length=30, default="Черный")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
