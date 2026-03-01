from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def design(request):
    return render(request, "design.html")