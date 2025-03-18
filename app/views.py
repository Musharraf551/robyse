from django.shortcuts import render
from app.models import *
from django.views.generic import DetailView
# Create your views here.
def home_view(request):
    cate= ItemList.objects.all()
    item = Items.objects.all()
    context = {'cate':cate, 'item':item}
    return render(request, 'home.html', context)

class Items_Detail(DetailView):
    model=More
    context_object_name='moreobj'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['more'] = self.object.More.all()  # Ensure students are retrieved
        return context