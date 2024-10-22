"""
URL configuration for note project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from noteapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listone/', views.listone, name='listone'),
    path('listall/', views.listall, name='listall'),
    path('insert/', views.insert, name='insert'),
    path('modify/<int:note_id>/', views.modify, name='modify'),  
    path('delete/<int:id>/', views.delete, name='delete'),    
    path('view_note/<int:note_id>/', views.view_note, name='view_note'),
    path('view_all/', views.view_all, name='view_all'),  
    path('delete_image/<int:image_id>/', views.delete_image, name='delete_image'),
    path('delete_pdf/<int:pdf_id>/', views.delete_pdf, name='delete_pdf'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
