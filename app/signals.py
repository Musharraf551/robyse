from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Booking


        
@receiver(post_save, sender=Booking)
def send_booking_confirmation_email(sender, instance, created, **kwargs):
    if created:  # Only send email when a new booking is created
        user_email = instance.user.email  # Now this is guaranteed to exist
        subject = "Booking Confirmation"
        message = f"Hello {instance.user.username},\n\nYour booking for {instance.name} on {instance.date} has been confirmed.\n\nThank you!"
        
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user_email],  # Send email to the user who booked
            fail_silently=False,
        )
