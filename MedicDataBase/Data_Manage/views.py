from django.shortcuts import render
from .models import Data_Manage

# Create your views here.

def index(request):
    data = Data_Manage.objects.all()
    return render(request, "index.html", {"data": data})