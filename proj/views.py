from django.http import FileResponse
import os
from .models import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.conf import settings

def resume_pdf(request):
    pdf_path = os.path.join(settings.MEDIA_ROOT, 'resume-simar.pdf')
    return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')

def index(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['comment']
        
        # Save to database
        new_contact = ContactForm(name=name, email=email, comment=comment)
        new_contact.save()
        
        # Send email
        send_mail(
            f"New Contact Form Submission from {name}",
            f"Name: {name}\nEmail: {email}\nMessage: {comment}",
            settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_FORM_EMAIL],
            fail_silently=False,
        )
        
    return render(request, 'index.html', {})
