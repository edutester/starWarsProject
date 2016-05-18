from django.shortcuts import render

from .models import Soldier

# Create your views here.

def index(request):
	soldiers = Soldier.objects.all()
	return render(
		request, 
		'cloneTroopersApp/index.html', 
		{'soldiers': soldiers},
	)

