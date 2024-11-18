from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.

from .models import Patient , Medicalrecord , Medicalimage

def patient_list(request):
    query = request.GET.get('q')
    if query:
        patients = Patient.objects.filter(name__icontains=query)
    else:
        patients = Patient.objects.all()
    return render(request, 'patient.html', {'patients': patients})

def patient_detail(request, patient_id):
    patient = get_object_or_404(Patient, patientid=patient_id)
    medical_records = Medicalrecord.objects.filter(patientid=patient_id)
    medical_images = Medicalimage.objects.filter(recordid__in=medical_records.values_list('recordid', flat=True))
    return render(request, 'patient_detail.html', {
        'patient': patient,
        'medical_records': medical_records,
        'medical_images': medical_images
    })


def patient_pdf(request, patient_id, field_name):
    medical_record = get_object_or_404(Medicalrecord, patientid=patient_id)
    pdf_data = getattr(medical_record, field_name, None)
    if pdf_data is None:
        return HttpResponse("Field not found", status=404)
    response = HttpResponse(pdf_data, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{field_name}.pdf"'
    return response

def patient_image(request, image_id):
    medical_image = get_object_or_404(Medicalimage, imageid=image_id)
    image_data = None
    content_type = 'image/jpeg'
    if medical_image.ctimage:
        image_data = medical_image.ctimage
    elif medical_image.mriimage:
        image_data = medical_image.mriimage
        content_type = 'image/bmp'
    elif medical_image.ultrasoundimage:
        image_data = medical_image.ultrasoundimage
        content_type = 'image/png'
    if image_data is None:
        return HttpResponse("Image not found", status=404)
    response = HttpResponse(image_data, content_type=content_type)
    return response