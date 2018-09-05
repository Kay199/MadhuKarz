from django.urls import path

from . import views



app_name = 'car'

urlpatterns = [
#/car/
path('', views.AvailableCarsView.as_view(), name ='AvailableCars'),
#/car/123/
path('<int:pk>/', views.CarDetailView.as_view(), name='detail'),

]
