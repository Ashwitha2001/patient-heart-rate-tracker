from django.contrib import admin
from .models import Profile,Patient, HeartRate

admin.site.register(Profile)
admin.site.register(Patient)
admin.site.register(HeartRate)
