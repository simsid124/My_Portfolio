from django.db import models

class ContactForm(models.Model):
    name= models.CharField(max_length=50, blank=False, null=False)
    email= models.EmailField()
    comment= models.TextField()
    
    def __str__(self):
        return self.name