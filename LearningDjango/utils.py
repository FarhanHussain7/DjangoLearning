from django.core.mail import send_mail
from django.conf import settings

def send_contact_email(request):
    """
    Simple utility function to send a test email.
    
    Parameters:
    request (HttpRequest): The current HTTP request (not used in this simple version).
    
    Returns:
    None: This function doesn't return anything.
    """
    subject = "This is a test email from Django"
    message = "This is a test email sent from Django."
    from_email = settings.EMAIL_HOST_USER
    recipient_email = 'fh4456200@gmail.com'  # Fixed typo: receive_email -> recipient_email
    
    try:
        send_mail(
            subject, 
            message, 
            from_email, 
            [recipient_email]
        )
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Error sending email: {e}")