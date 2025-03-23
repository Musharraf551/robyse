from django import forms
from .models import *

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'time_slot', 'number_of_people']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time_slot': forms.TextInput(attrs={'placeholder': 'e.g., 10:00 AM - 12:00 PM'}),
            'number_of_people': forms.NumberInput(attrs={'min': 1}),
        }
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user  # Store the user instance if needed
        
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment','rating']
        widgets = {
            # 'reviewer_name': forms.TextInput(attrs={'type': 'text'}),
            # 'date': forms.DateInput(attrs={'type': 'date'}),
            
            'comment': forms.TextInput(attrs={'type': 'text'}),
            'rating': forms.NumberInput(attrs={'min': 1}),    
        }
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user  # Store the user instance if needed