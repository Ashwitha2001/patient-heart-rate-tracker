from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.utils.dateparse import parse_date
from .models import Patient, HeartRate
from .serializers import PatientSerializer, HeartRateSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    if User.objects.filter(username=username).exists():
        return Response({'message': 'Username already exists!'}, status=400)
    
    if User.objects.filter(email=email).exists():
        return Response({'message': 'Email already exists!'}, status=400)

    user = User.objects.create_user(username=username, email=email, password=password)
    return Response({'message': 'User registered successfully!'}, status=201)


@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)

    if user:
        return Response({'message': 'Login successful!'})
    return Response({'message': 'Invalid credentials!'}, status=400)



@api_view(['GET'])
def patient_list(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=404)

    patients = Patient.objects.filter(user=user)
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def patient_create(request):
    serializer = PatientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)



class HeartRatePagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50



@api_view(['GET'])
def heart_rate_list(request, patient_id):
    try:
        patient = Patient.objects.get(id=patient_id)
    except Patient.DoesNotExist:
        return Response({'error': 'Patient not found'}, status=404)

    heart_rates = HeartRate.objects.filter(patient=patient)

    start_date = request.query_params.get('start_date')
    end_date = request.query_params.get('end_date')

    if start_date:
        heart_rates = heart_rates.filter(recorded_at__gte=parse_date(start_date))
    if end_date:
        heart_rates = heart_rates.filter(recorded_at__lte=parse_date(end_date))

    paginator = HeartRatePagination()
    paginated_results = paginator.paginate_queryset(heart_rates, request)
    serializer = HeartRateSerializer(paginated_results, many=True)
    
    return paginator.get_paginated_response(serializer.data)



@api_view(['POST'])
def heart_rate_create(request, patient_id):
    try:
        patient = Patient.objects.get(id=patient_id)
    except Patient.DoesNotExist:
        return Response({'error': 'Patient not found'}, status=404)

    data = request.data
    data['patient'] = patient_id  

    if 'heart_rate' not in data:
        return Response({'error': 'heart_rate field is required'}, status=400)

    serializer = HeartRateSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    
    return Response(serializer.errors, status=400)
