from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def students(request):
    return HttpResponse("List of students")