from django.db import models
from django.contrib.auth.models import User

class Diabetes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pregnancies = models.IntegerField(default = 0)
    glucose = models.IntegerField()
    blood_pressure = models.IntegerField()
    skin_thickness = models.IntegerField()
    insulin = models.IntegerField()
    bmi = models.FloatField()
    diabetes_pedigree_function = models.FloatField()
    age = models.IntegerField()
    outcome = models.FloatField(default=False) 

    
class PredictCardio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    Sexe = models.IntegerField()  
    chest_pain = models.IntegerField()  
    blood_pressure = models.FloatField()  
    cholestoral = models.IntegerField()  
    blood_sugar = models.IntegerField()  
    electrocardiographic = models.IntegerField()
    heart_rate = models.IntegerField()
    exercise = models.IntegerField()
    slope = models.IntegerField()
    Oldpeak = models.FloatField()
    major_vessels = models.IntegerField()
    Thalassemia = models.IntegerField()
    target = models.FloatField(default=0)

class Pneumonia(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos')
    target = models.FloatField(default=0)