from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import Car, Owner, Brand
from .serializers import CarSerializer, OwnerSerializer, BrandSerializer


class CarView(APIView):
    def get(self, request):
        cars = Car.objects.all()
        cars_serializers = CarSerializer(cars, many=True)
        return Response({'cars': cars_serializers.data}, status=status.HTTP_200_OK)

    def post(self, request: Request, pk) -> Response:
        if not pk:
            return Response({"messages": "Method POST not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            serializer = CarSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            car = serializer.save()
            return Response(CarSerializer(car).data, status=status.HTTP_201_CREATED)

    def put(self, request: Request, pk) -> Response:
        if not pk:
            return Response({'messegas by SISTEM':'This car does not exist'}, status=status.HTTP_404_NOT_FOUND)
        try:
            car = CarSerializer.object.get(pk=pk)
        except:
            return Response({'messegas by SISTEM':'This car does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        serializers = CarSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)

        car = serializers.save()

        return Response(CarSerializer(car).data, status=status.HTTP_200_OK)
    
    def delete(self, request: Response, pk) -> Response:
        if not pk:
            return Response({'messeges by SISTEM':'This car does not exist'})
        else:
            try:
                car = Car.objects.get(pk=pk)
            except Exception as e:
                return Response({'messeges by SISTEM'})
            
            car.delete()
        return Response({'messeges by SISTEM':'The car has deleted 💀'})



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
    
    def put(self, request: Request, pk) -> Response:
        if not pk:
            return Response({'messegas by SISTEM':'This car does not exist'}, status=status.HTTP_404_NOT_FOUND)
        try:
            car = OwnerSerializer.object.get(pk=pk)
        except:
            return Response({'messegas by SISTEM':'This car does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        serializers = OwnerSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)

        car = serializers.save()

        return Response(OwnerSerializer(car).data, status=status.HTTP_200_OK)
    
    def delete(self, request: Response, pk) -> Response:
        if not pk:
            return Response({'messeges by SISTEM':'This owner not exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                owner = Owner.objects.get(pk=pk)
            except Exception as e:
                return Response({'messeges by SISTEM':'Error with sistem'}, status=status.HTTP_404_NOT_FOUND)
            
            owner.delete()

            return Response({'messeges by SISTEM':'The owner has deleted 👻'})


class BrandView(APIView):
    def get(self, request: Response) -> Response:
        brands = Brand.objects.all()
        brands_serializers = BrandSerializer(brands, many=True)
        return Response({'brands':brands_serializers.data}, status=status.HTTP_200_OK)
    
    def post(self, request:Response, pk) -> Response:
        brand_serializer = BrandSerializer(data=request.data)
        if not pk:
            return Response({'messeges by SISTEM':'This brand not exist 🤖'}, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                brand_serializer.is_valid(raise_exception=True)
                brand_serializer.save()
            except Exception as e:
                return Response({'messeges by SISTEM':e}, status=status.HTTP_404_NOT_FOUND)
            
            return Response({'messeges by SISTEM':'Brand has created 🥳'})
        
    def put(self, request:Response, pk) -> Response:
        brend_serializer = Brand.objects.get(pk=pk)
        if pk:
            return Response({'messeges by SISTEM':'This brand not exisit'}, status=status.HTTP_404_NOT_FOUND)
        else:
            
            try:
                brend_serializer.is_valid(raise_exception=True)
                brend_serializer.save()
            except:
                return Response({'messegesby by SISTEM':'Error on sistem'}, status=status.HTTP_404_NOT_FOUND)

            return Response(BrandSerializer(brend_serializer.data, status=status.HTTP_200_OK))
        
    def delete(self, request:Response, pk) -> Response:
        if not pk:
            return Response({'messeges by SISTEM':'This brand not exist 🤖'}, status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                brand = Brand.objects.get(pk=pk)
            except Exception as e:
                return Response({'messeges by SISTEM':'Error on sistem'}, status=status.HTTP_404_NOT_FOUND)
            
            brand.delete()
            return Response({'messeges by SISTEM':'Brand has deleted 🥲'})