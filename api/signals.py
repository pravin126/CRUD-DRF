from django.db.models.signals import post_save
from django.dispatch import receiver
from .admin import PostModelAdmin

@receiver(post_save, sender=PostModelAdmin)
def send_post_creation_email(sender, instance, created, **kwargs):
    if created:
        # Send an email to the author here.
        # You can use Django's EmailMessage or a third-party package like Django's built-in `send_mail`.

        subject = "New Post Created"
        message = "Your new post has been created."
        from_email = "pravinkalokhe5@gmail.com.com"
        recipient_list = [instance.author.email]  # Assuming author is a ForeignKey in your post model.

        # Send the email.
        send_mail(subject, message, from_email, recipient_list)
