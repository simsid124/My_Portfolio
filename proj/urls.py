from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import resume_pdf

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('resume-simar-pdf/', views.resume_pdf, name='resume-simar_pdf'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

