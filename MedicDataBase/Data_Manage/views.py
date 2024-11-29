from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.

from .models import Patient , Medicalrecord , Medicalimage , Devicedata , Genomicdata , Temperature , Audiorecord , Department , Doctor , Document , Hospital , Standardvideo

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
    device_datas = Devicedata.objects.filter(patientid=patient_id)
    genomic_datas = Genomicdata.objects.filter(patientid=patient_id)
    patient_temperatures = Temperature.objects.filter(patientid=patient_id)
    return render(request, 'patient_detail.html', {
        'patient': patient,
        'medical_records': medical_records,
        'medical_images': medical_images,
        'device_datas': device_datas,
        'genomic_datas': genomic_datas,
        'patient_temperatures': patient_temperatures
    })

def device_pdf(request, data_id):
    device_data = get_object_or_404(Devicedata, dataid=data_id)
    pdf_data = device_data.datacontent
    if pdf_data is None:
        return HttpResponse("PDF not found", status=404)
    response = HttpResponse(pdf_data, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="device_data_{data_id}.pdf"'
    return response

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

def genomic_data(request, gene_id, field_name):
    genomic_data = get_object_or_404(Genomicdata, geneid=gene_id)
    file_data = getattr(genomic_data, field_name, None)
    if file_data is None:
        return HttpResponse("Field not found", status=404)
    content_type = 'application/octet-stream'
    if field_name == 'genesequence':
        content_type = 'application/fasta'
    response = HttpResponse(file_data, content_type=content_type)
    response['Content-Disposition'] = f'attachment; filename="{field_name}_{gene_id}.{field_name.split("sequence")[-1] if field_name == "genesequence" else "pdf"}"'
    return response

def patient_temperature(request, patient_id):
    temperature_data = get_object_or_404(Temperature, patient_id=patient_id)
    return render(request, 'patient_temperature.html', {'temperature_data': temperature_data})

def temperature_image(request, temperature_id):
    temperature = get_object_or_404(Temperature, dataid=temperature_id)
    image_data = temperature.image
    if image_data is None:
        return HttpResponse("Image not found", status=404)
    response = HttpResponse(image_data, content_type='image/jpeg')
    return response

def temperature_source(request, temperature_id):
    temperature = get_object_or_404(Temperature, dataid=temperature_id)
    file_data = temperature.sourcefile
    if file_data is None:
        return HttpResponse("File not found", status=404)
    response = HttpResponse(file_data, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="temperature_{temperature_id}.csv"'
    return response