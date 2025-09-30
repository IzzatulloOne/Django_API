from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import Car, Owner
from .serializers import CarSerializer, OwnerSerializer


class CarListView(APIView):
    def get(self, request):
        car = Car.objects.all()
        car_serializer = CarSerializer(car, many=True)
        return Response({'cars': car_serializer.data}, status=status.HTTP_200_OK)


class OwnerListView(APIView):
    def get(self, request):
        owner = Owner.objects.all()
        owner_serializer = OwnerSerializer(owner, many=True)
        return Response({'owners': owner_serializer.data}, status=status.HTTP_200_OK)
    

class CreateCarView(APIView):
    def post(self, request: Request) -> Response:
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CreateOwnerView(APIView):
    def post(self, request: Request) -> Response:
        serializer = OwnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)