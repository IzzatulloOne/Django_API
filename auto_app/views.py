from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import Car, Owner
from .serializers import CarSerializer, OwnerSerializer


class CarView(APIView):
    def get(self, request):
        cars = Car.objects.all()
        cars_serializers = CarSerializer(cars, many=True)
        return Response({'cars': cars_serializers.data}, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        car_serializers = CarSerializer(data=request.data)
        try:
            car_serializers.is_valid(raise_exception=True)
            car_serializers.save()
            return Response(car_serializers.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class OwnerView(APIView):
    def get(self, request):
        owners = Owner.objects.all()
        owner_serializers = OwnerSerializer(owners, many=True)
        return Response({'owners': owner_serializers.data}, status=status.HTTP_200_OK)
    
    def post(self, request: Request) -> Response:       
        owner_serializers = OwnerSerializer(data=request.data)
        try:
            owner_serializers.is_valid(raise_exception=True)
            owner_serializers.save()
            return Response(owner_serializers.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        