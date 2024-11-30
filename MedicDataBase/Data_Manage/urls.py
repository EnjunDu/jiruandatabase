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
    path('temperature_image/<int:temperature_id>/', views.temperature_image, name='temperature_image'),
    path('temperature_source/<int:temperature_id>/', views.temperature_source, name='source_temperature'),

    path('patients/<int:patient_id>/bloodsugar/', views.patient_bloodsugar, name='patient_bloodsugar'),
    path('bloodsugar_image/<int:bloodsugar_id>/', views.bloodsugar_image, name='bloodsugar_image'),
    path('bloodsugar_source/<int:bloodsugar_id>/', views.bloodsugar_source, name='source_bloodsugar'),

    path('patients/<int:patient_id>/bloodpressure/', views.patient_bloodpressure, name='patient_bloodpressure'),
    path('bloodpressure_image/<int:bloodpressure_id>/', views.bloodpressure_image, name='bloodpressure_image'),
    path('bloodpressure_source/<int:bloodpressure_id>/', views.bloodpressure_source, name='source_bloodpressure'),
]