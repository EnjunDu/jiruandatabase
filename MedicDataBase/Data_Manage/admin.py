from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Audiorecord)
admin.site.register(Department)
admin.site.register(Devicedata)
admin.site.register(Doctor)
admin.site.register(Document)
admin.site.register(Genomicdata)
admin.site.register(Hospital)
admin.site.register(Patient)
admin.site.register(Standardvideo)
admin.site.register(Temperature)
admin.site.register(Bloodpressure)
admin.site.register(Bloodsugar)
