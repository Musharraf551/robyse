from django.shortcuts import render
from app.models import *
# Create your views here.
def home_view(request):
    cate= ItemList.objects.all()
    item = Items.objects.all()
    context = {'cate':cate, 'item':item}
    return render(request, 'home.html', context)
