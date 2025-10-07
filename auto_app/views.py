from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Car, Owner, Brand
from .serializers import CarSerializer, OwnerSerializer, BrandSerializer
from .permissions import MyCustomPermissions
from .paginator import CustomPagination


class AdminUpdateOnly(permissions.BasePermission):  
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class CarView(generics.ListCreateAPIView):
    queryset = Car.objects.order_by('-id')
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly | MyCustomPermissions]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'brand', 'model', 'year', 'engine_type', 'transmission', 'color__name', 'owner__name']
    search_fields = ['brand', 'model', 'year', 'engine_type', 'transmission', 'color__name', 'owner__name']
    ordering_fields = ['id', 'brand', 'model', 'year', 'engine_type', 'transmission', 'color__name', 'owner__name']
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        return self.list(request,*args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self,request, *args, **kwargs):
        return self.list(request,*args,**kwargs)

    def delete(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class OwnerView(generics.ListCreateAPIView):
    queryset = Owner.objects.order_by('-id')
    serializer_class = OwnerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly | AdminUpdateOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'name', 'email', 'phone']
    search_fields = ['name', 'email', 'phone']
    ordering_fields = ['id', 'name', 'email', 'phone']
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        return self.list(request,*args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self,request, *args, **kwargs):
        return self.list(request,*args,**kwargs)

    def delete(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class BrandView(generics.ListCreateAPIView):
    queryset = Brand.objects.order_by('-id')
    serializer_class = BrandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly | AdminUpdateOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'name', 'since']
    search_fields = ['name', 'since']
    ordering_fields = ['id', 'name', 'since']
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        return self.list(request,*args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self,request, *args, **kwargs):
        return self.list(request,*args,**kwargs)

    def delete(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class GetCarView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly | AdminUpdateOnly]
    
class GetOwnerView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    permission_classes = [permissions.IsAdminUser]


class GetBrandView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly | AdminUpdateOnly]


# class CarView(APIView):
#     def get(self, request):
#         cars = Car.objects.all()
#         cars_serializers = CarSerializer(cars, many=True)
#         return Response({'cars': cars_serializers.data}, status=status.HTTP_200_OK)

#     def post(self, request: Request, pk) -> Response:
#         if not pk:
#             return Response({"messages": "Method POST not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         else:
#             serializer = CarSerializer(data=request.data)
#             serializer.is_valid(raise_exception=True)

#             car = serializer.save()
#             return Response(CarSerializer(car).data, status=status.HTTP_201_CREATED)

#     def put(self, request: Request, pk) -> Response:
#         if not pk:
#             return Response({'messegas by SISTEM':'This car does not exist'}, status=status.HTTP_404_NOT_FOUND)
#         try:
#             car = CarSerializer.object.get(pk=pk)
#         except:
#             return Response({'messegas by SISTEM':'This car does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
#         serializers = CarSerializer(data=request.data)
#         serializers.is_valid(raise_exception=True)

#         car = serializers.save()

#         return Response(CarSerializer(car).data, status=status.HTTP_200_OK)
    
#     def delete(self, request: Response, pk) -> Response:
#         if not pk:
#             return Response({'messeges by SISTEM':'This car does not exist'})
#         else:
#             try:
#                 car = Car.objects.get(pk=pk)
#             except Exception as e:
#                 return Response({'messeges by SISTEM'})
            
#             car.delete()
#         return Response({'messeges by SISTEM':'The car has deleted 💀'})


# class OwnerView(APIView):
#     def get(self, request):
#         owners = Owner.objects.all()
#         owner_serializers = OwnerSerializer(owners, many=True)
#         return Response({'owners': owner_serializers.data}, status=status.HTTP_200_OK)
    
#     def post(self, request: Request) -> Response:       
#         owner_serializers = OwnerSerializer(data=request.data)
#         try:
#             owner_serializers.is_valid(raise_exception=True)
#             owner_serializers.save()
#             return Response(owner_serializers.data, status=status.HTTP_201_CREATED)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
#     def put(self, request: Request, pk) -> Response:
#         if not pk:
#             return Response({'messegas by SISTEM':'This car does not exist'}, status=status.HTTP_404_NOT_FOUND)
#         try:
#             car = OwnerSerializer.object.get(pk=pk)
#         except:
#             return Response({'messegas by SISTEM':'This car does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
#         serializers = OwnerSerializer(data=request.data)
#         serializers.is_valid(raise_exception=True)

#         car = serializers.save()

#         return Response(OwnerSerializer(car).data, status=status.HTTP_200_OK)
    
#     def delete(self, request: Response, pk) -> Response:
#         if not pk:
#             return Response({'messeges by SISTEM':'This owner not exist'}, status=status.HTTP_404_NOT_FOUND)
#         else:
#             try:
#                 owner = Owner.objects.get(pk=pk)
#             except Exception as e:
#                 return Response({'messeges by SISTEM':'Error with sistem'}, status=status.HTTP_404_NOT_FOUND)
            
#             owner.delete()

#             return Response({'messeges by SISTEM':'The owner has deleted 👻'})


# class BrandView(APIView):
#     def get(self, request: Response) -> Response:
#         brands = Brand.objects.all()
#         brands_serializers = BrandSerializer(brands, many=True)
#         return Response({'brands':brands_serializers.data}, status=status.HTTP_200_OK)
    
#     def post(self, request:Response, pk) -> Response:
#         brand_serializer = BrandSerializer(data=request.data)
#         if not pk:
#             return Response({'messeges by SISTEM':'This brand not exist 🤖'}, status=status.HTTP_404_NOT_FOUND)
#         else:
#             try:
#                 brand_serializer.is_valid(raise_exception=True)
#                 brand_serializer.save()
#             except Exception as e:
#                 return Response({'messeges by SISTEM':e}, status=status.HTTP_404_NOT_FOUND)
            
#             return Response({'messeges by SISTEM':'Brand has created 🥳'})
        
#     def put(self, request:Response, pk) -> Response:
#         brend_serializer = Brand.objects.get(pk=pk)
#         if pk:
#             return Response({'messeges by SISTEM':'This brand not exisit'}, status=status.HTTP_404_NOT_FOUND)
#         else:
            
#             try:
#                 brend_serializer.is_valid(raise_exception=True)
#                 brend_serializer.save()
#             except:
#                 return Response({'messegesby by SISTEM':'Error on sistem'}, status=status.HTTP_404_NOT_FOUND)

#             return Response(BrandSerializer(brend_serializer.data, status=status.HTTP_200_OK))
        
#     def delete(self, request:Response, pk) -> Response:
#         if not pk:
#             return Response({'messeges by SISTEM':'This brand not exist 🤖'}, status=status.HTTP_404_NOT_FOUND)
#         else:
#             try:
#                 brand = Brand.objects.get(pk=pk)
#             except Exception as e:
#                 return Response({'messeges by SISTEM':'Error on sistem'}, status=status.HTTP_404_NOT_FOUND)
            
#             brand.delete()
#             return Response({'messeges by SISTEM':'Brand has deleted 🥲'})
        