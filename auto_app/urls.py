from django.urls import path
from .views import CarListView, OwnerListView, CreateCarView, CreateOwnerView   

urlpatterns = [
    path('car_list/', CarListView.as_view()),
    path('owner_list/', OwnerListView.as_view()),
    path('create_car/', CreateCarView.as_view()),
    path('create_owner/', CreateOwnerView.as_view()),
]