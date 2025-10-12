from django.urls import path
from .views import (
    CarView, GetCarView,
    OwnerView, GetOwnerView,
    BrandView, GetBrandView,
)

app_name = 'auto_app'

urlpatterns = [

    path('cars/', CarView.as_view(), name='cars-list-create'),
    path('cars/<int:pk>/', GetCarView.as_view(), name='cars-detail'),

    
    path('owners/', OwnerView.as_view(), name='owners-list-create'),
    path('owners/<int:pk>/', GetOwnerView.as_view(), name='owners-detail'),

    
    path('brands/', BrandView.as_view(), name='brands-list-create'),
    path('brands/<int:pk>/', GetBrandView.as_view(), name='brands-detail'),
]
