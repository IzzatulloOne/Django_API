from django.urls import path
from .views import CarView, OwnerView

urlpatterns = [
    path('car_list/', CarView.as_view()),
    path('owner_list/', OwnerView.as_view()),
]   