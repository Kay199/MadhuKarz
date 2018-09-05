from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView
#from django.contrib.auth.decorators import login_required    

from .forms import CustomUserCreationForm
from .models import reservation, Rental_Invoice
from car.models import Car


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'



# I wanna auto fill the car_id that I pass from the html 
class CarReservation(CreateView):
	model = reservation

	def get_initial(self):
		print(self.kwargs['pk'])
		return {'car_id' : self.kwargs['pk']}
	
	fields = ['car_id','pick_location_id', 'dropoff_location_id', 'start_date', 'end_date', 'remarks', 'fuel_option_id', 'rental_insurance_id']


class RentalInvoiceDetailView(generic.DetailView):
    model = Rental_Invoice
    template_name = 'car/invoicedetail.html'