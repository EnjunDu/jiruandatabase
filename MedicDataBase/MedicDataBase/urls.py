"""
URL configuration for MedicDataBase project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include , path
from data_manage import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('data_manage.urls')),  # 替换为您的应用名称
    path('patients/<int:patient_id>/pdf/<str:field_name>/', views.patient_pdf, name='patient_pdf'),
    path('patients/image/<int:image_id>/', views.patient_image, name='patient_image'),
]
