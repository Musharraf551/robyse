from django.shortcuts import render, get_object_or_404, redirect
from app.models import *
from app.forms import *

# Create your views here.
def home_view(request):
    categories = Category.objects.all()
    instances = Model1.objects.all()
    return render(request, 'home.html', {'categories': categories, 'instances': instances})

def instance_detail(request, pk):
    instance = get_object_or_404(Model1, pk=pk)
    reviews = instance.reviews.all()
    return render(request, 'instance_detail.html', {'instance': instance, 'reviews':reviews})

def booking_view(request, pk):
    instance = get_object_or_404(Model1, pk=pk)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.instance = instance
            booking.name = instance.name  # Auto-fill name
            booking.price = instance.price  # Auto-fill price
            booking.save()
            return redirect('booking_success')  # Redirect to a success page
    
    else:
        form = BookingForm()

    return render(request, 'booking_form.html', {'form': form, 'instance': instance})

def booking_success(request):
    return render(request, 'booking_success.html')

def feedback_view(request, pk):
    instance = get_object_or_404(Model1, pk=pk)  # Get the related object

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.name = instance  # Assign ForeignKey object, not instance.name
            feedback.save()
            return redirect('home')  # Redirect to home or success page
    
    else:
        form = FeedbackForm()  # Fixed: Use FeedbackForm

    return render(request, 'feedback_form.html', {'form': form, 'instance': instance})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    instances = Model1.objects.filter(category=category)  # Filter instances by category

    return render(request, 'category_detail.html', {'category': category, 'instances': instances})
