from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Booking

@receiver(post_save, sender=Booking)
def send_booking_confirmation_email(sender, instance, created, **kwargs):
    if created:  # Send email only when a new booking is created
        subject = "Your Hotel Booking Confirmation"
        message = f"Hello {instance.user.username},\n\n"
        message += f"Your booking for {instance.instance.name} is confirmed!\n"
        message += f"📍 Location: {instance.instance.location}\n"
        message += f"💰 Price: ${instance.price}\n"
        message += f"📅 Date: {instance.date}\n"
        message += f"⏰ Time Slot: {instance.time_slot}\n"
        message += f"👥 Guests: {instance.number_of_people}\n\n"
        message += "Thank you for choosing our service!\nBest regards,\nHotel Management Team"

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [instance.user.email],  # Send email to the user who booked
            fail_silently=False,
        )
