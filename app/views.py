from django.shortcuts import render
from app.models import *
from django.views.generic import DetailView
# Create your views here.
def home_view(request):
    categories = Category.objects.all()
    instances = Model1.objects.all()
    return render(request, 'home.html', {'categories': categories, 'instances': instances})

