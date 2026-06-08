from django.contrib import admin
from .models import Diabetes,PredictCardio,Pneumonia
# Register your models here.
admin.site.register(Diabetes)
admin.site.register(PredictCardio)
admin.site.register(Pneumonia)