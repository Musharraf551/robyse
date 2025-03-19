from django.shortcuts import render, get_object_or_404
from app.models import *
from django.views.generic import DetailView
# Create your views here.
def home_view(request):
    categories = Category.objects.all()
    instances = Model1.objects.all()
    return render(request, 'home.html', {'categories': categories, 'instances': instances})

def instance_detail(request, pk):
    instance = get_object_or_404(Model1, pk=pk)
    reviews = instance.reviews.all()
    return render(request, 'instance_detail.html', {'instance': instance, 'reviews':reviews})