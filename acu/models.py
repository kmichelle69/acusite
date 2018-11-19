from django.db import models

class Symptom(models.Model):
    symptom_text = models.CharField(max_length=200)
    def __str__(self):
        return self.symptom_text

class Diagnosis(models.Model):
    symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)
    diagnosis_text = models.CharField(max_length=200)
    def __str__(self):
        return self.diagnosis_text
