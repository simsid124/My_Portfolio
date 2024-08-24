from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
import os
from .models import ContactForm
from django.conf import settings

def resume_pdf(request):
<<<<<<< HEAD
    pdf_path = os.path.join(settings.MEDIA_ROOT, 'resume-simar.pdf')
=======
    pdf_path = os.path.join(settings.MEDIA_ROOT, 'resume_simar.pdf')
>>>>>>> 1fd53bc81600c97dba14ba080ca23a590d233dfb
    return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')

def index(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['comment']
        
        new_contact = ContactForm(name=name, email=email, comment=comment)
        new_contact.save()
        
    return render(request, 'index.html', {})