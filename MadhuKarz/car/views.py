from django.views import generic
from django.http import HttpResponse
from .models import Car

class AvailableCarsView(generic.ListView):
	template_name = 'car/availablecars.html'
	context_object_name = 'available_cars'

	def get_queryset(self):
		return Car.objects.filter(status=True)

class CarDetailView(generic.DetailView):
#class CarDetailView(generic.DetailView,pk):
    model = Car
    
    
    #def get_object(self):
    #	print(self.kwargs['pk'])

    template_name = 'car/cardetail.html'


