from django.contrib import admin
from .models import Owner, Car

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'sex')
    search_fields = ('name',)
    list_filter = ('sex',)
    ordering = ('name',)    
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'age', 'sex')
        }),
    )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model', 'year', 'owner')
    search_fields = ('brand', 'model', 'owner__name')
    list_filter = ('brand', 'year', 'engine_type', 'transmission', 'drive_type', 'body_type')
    ordering = ('-year', 'brand', 'model')
    fieldsets = (
        ('Основная информация', {
            'fields': ('owner', 'brand', 'model', 'year', 'body_type')
        }),
        ('Двигатель и трансмиссия', {
            'fields': ('engine_type', 'engine_volume', 'horsepower', 'torque', 'transmission', 'drive_type')
        }),
        ('Размеры и вес', {
            'fields': ('length', 'width', 'height', 'wheelbase', 'weight')
        }),
        ('Динамика и расход', {
            'fields': ('acceleration_0_100', 'max_speed', 'fuel_consumption')
        }),
        ('Безопасность и комфорт', {
            'fields': ('safety_rating', 'seats', 'has_air_conditioner', 'has_multimedia')
        }),
    )