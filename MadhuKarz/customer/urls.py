from django.urls import path
from . import views


app_name = 'customer'

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
	#/customer/reservation/ 
	path('<int:pk>/reservation/', views.CarReservation.as_view(), name='CarReservation'),
	#/customer/342/invoicepayment/
	path('<int:pk>/invoicepayment/', views.RentalInvoiceDetailView.as_view(), name='invoicepayment'),
	
]
