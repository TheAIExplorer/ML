from .views import predict_car_brand
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path('predict_car_brand/',
         views.predict_car_brand, name='car_brand'),
    # path('predict_landmarks/', views.predict_landmarks, name='predict_landmarks'),
]
