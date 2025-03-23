from django.shortcuts import render, get_object_or_404, redirect
from app.models import *
from app.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


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
        form = BookingForm(request.POST, user = request.user)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.instance = instance
            booking.name = instance.name  # Auto-fill name
            booking.price = instance.price  # Auto-fill price
            booking.user = request.user
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
        form = FeedbackForm(request.POST, user = request.user)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.instance = instance  # Assign ForeignKey object, not instance.name
            feedback.name=instance.name
            feedback.user = request.user
            feedback.save()
            return redirect('home_view')  # Redirect to home or success page
    
    else:
        form = FeedbackForm(user = request.user)  # Fixed: Use FeedbackForm

    return render(request, 'feedback_form.html', {'form': form, 'instance': instance})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    instances = Model1.objects.filter(category=category)  # Filter instances by category

    return render(request, 'category_detail.html', {'category': category, 'instances': instances})

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Your account has been created! Please log in.')
#             return redirect('login')
#     else:
#         form = UserCreationForm()

#     return render(request, 'signup.html', {'form': form})
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in user after signup
            return redirect("home_view")  # Redirect to home page
    else:
        form = CustomUserCreationForm()
    return render(request, "signup.html", {"form": form})

def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Ensure 'dashboard' is correctly mapped in urls.py
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'login.html')

def LogoutView(request):
    logout(request)  # Logs the user out
    return redirect('Home')  # Redirects to the home page

@login_required
def dashboard(request):
    user = request.user
    feedbacks = user.feedback.all()
    bookings = user.booking.all()  
    return render(request, 'dashboard.html', {'feedbacks':feedbacks,'bookings': bookings})

def about(request):
    obj = About.objects.all()
    d = {'obj': obj}
    return render(request, 'about.html', d)