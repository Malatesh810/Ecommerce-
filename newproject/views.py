from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, 'new.html')
def add(request):
    return render(request, 'new.html')