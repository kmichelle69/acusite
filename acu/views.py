from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Symptom

def index(request):
    return HttpResponse("Hello this is the home page")



def symptoms(request):

    # add_symptoms = []
    #
    # if request.POST:
    #     if request.POST.getlist('symptom'):
    #         user.symptom = True
    #     else:
    #         user.symptom = False

        template = loader.get_template('acu/symptoms.html')
        # context = {
        #     'add symptoms': add_symptoms,
        # }

        return HttpResponse(template.render(request))



def diagnosis(request, diagnosis_text):
    response = "You are dying in the following way:"
    return HttpResponse(response % question_text)
