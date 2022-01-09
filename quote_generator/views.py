from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'quote_generator/index.html')

# Create your views here.
def about(request):
    return render(request, 'quote_generator/about.html')
# Create your views here.
