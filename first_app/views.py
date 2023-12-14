from django.shortcuts import render
from static import data
# Create your views here.

def index(request):
    return render(request, 'index.html', {'data': data})