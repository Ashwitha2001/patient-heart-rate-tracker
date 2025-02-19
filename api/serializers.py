from rest_framework import serializers
from .models import Patient, HeartRate

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

    def validate_age(self, value):
        if value <= 0:
            raise serializers.ValidationError("Age must be a positive number.")
        return value

    def validate_gender(self, value):
        if value.lower() not in ["male", "female", "other"]:
            raise serializers.ValidationError("Gender must be Male, Female, or Other.")
        return value


class HeartRateSerializer(serializers.ModelSerializer):
    heart_rate_status = serializers.SerializerMethodField()

    class Meta:
        model = HeartRate
        fields = ['id', 'patient', 'heart_rate', 'recorded_at', 'heart_rate_status']

    def validate_heart_rate(self, value):
        if value < 30 or value > 220:
            raise serializers.ValidationError("Heart rate must be between 30 and 220.")
        return value

    def get_heart_rate_status(self, obj):
        if obj.heart_rate < 60:
            return "Low"
        elif 60 <= obj.heart_rate <= 100:
            return "Normal"
        else:
            return "High"
