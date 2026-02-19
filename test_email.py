#!/usr/bin/env python
"""
Email Test Script
Test Django email configuration without running the full server
"""

import os
import django
from django.core.mail import send_mail
from django.conf import settings

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LearningDjango.settings')
django.setup()

def test_email():
    """Test email sending functionality"""
    print("Testing Django Email Configuration...")
    print(f"Email Backend: {settings.EMAIL_BACKEND}")
    print(f"SMTP Host: {settings.EMAIL_HOST}:{settings.EMAIL_PORT}")
    print(f"From: {settings.DEFAULT_FROM_EMAIL}")
    print(f"TLS: {settings.EMAIL_USE_TLS}")
    print("-" * 50)
    
    try:
        # Send test email
        send_mail(
            subject='Django Email Test - Successful!',
            message='This is a test email from Django application. If you receive this, email configuration is working correctly!',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.EMAIL_HOST_USER],  # Send to self for testing
            fail_silently=False,
        )
        print("✅ Email sent successfully!")
        print("Check your inbox for the test email.")
        
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        print("Please check:")
        print("1. App password is correct")
        print("2. Gmail 'Less secure app access' is enabled")
        print("3. Network connection is working")

if __name__ == "__main__":
    test_email()
