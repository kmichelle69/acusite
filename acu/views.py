from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Symptom

def index(request):
    return HttpResponse("Hello this is the home page")



def symptoms(request):
    # this is my form handler for symptoms.html
    # yes


    template = loader.get_template('acu/symptoms.html')


    return render(request, 'acu/symptoms.html')



def diagnosis(request, diagnosis_text):
    response = "You are dying in the following way:"
    return HttpResponse(response % question_text)
