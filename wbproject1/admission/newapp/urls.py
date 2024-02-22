from django.contrib import admin
from django.urls import path
from .views import*
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',homepage,name='homepage'),
path('view/',student_list,name='student_list'),
path('add/',add_student,name='add_student'),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)