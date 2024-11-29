from django.urls import path , include
from . import views

urlpatterns = [
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/<int:patient_id>/', views.patient_detail, name='patient_detail'),
    path('patients/<int:patient_id>/pdf/<str:field_name>/', views.patient_pdf, name='patient_pdf'),
    path('patients/image/<int:image_id>/', views.patient_image, name='patient_image'),
    path('patients/device_pdf/<int:data_id>/', views.device_pdf, name='device_pdf'),

    path('patients/genomic_data/<int:gene_id>/<str:field_name>/', views.genomic_data, name='genomic_data'),

    path('patients/<int:patient_id>/temperature/', views.patient_temperature, name='patient_temperature'),
    path('patients/image/<int:image_id>/temperature/', views.temperature_image, name='image_temperature'),
    path('patients/source/temperature/<int:file_id>/', views.temperature_source, name='source_temperature'),
]