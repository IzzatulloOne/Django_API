from django.urls import path
from .views import CarView, OwnerView, BrandView

urlpatterns = [
    path('car_list/', CarView.as_view()),
    path('owner_list/', OwnerView.as_view()),
    path('brand_list/', BrandView.as_view()),
]   