from core.models import User, UserProfile
from django.conf import settings  # To get DEFAULT_FROM_EMAIL
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Signal to create a UserProfile instance when a User is created."""
    if created:
        UserProfile.objects.get_or_create(user=instance)

@receiver(post_save, sender=User) 
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = "Welcome to JobSite"
        message = f"Hi {instance.first_name},\n\nThank you for registering at JobSite."
        from_email = settings.DEFAULT_FROM_EMAIL  # recommended to set this in your settings.py
        send_mail(subject, message, from_email, [instance.email])
