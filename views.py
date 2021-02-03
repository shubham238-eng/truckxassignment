from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Alarmserializer

from .models import AlarmTable


@api_view(['GET'])
def alarmList(request, imei):
    alarm = AlarmTable.objects.get(Imei=imei)
    serializer = Alarmserializer(alarm, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def alarmWithFilter(request, imei, start_time, end_time, alarm_type):
    alarms = AlarmTable.objects.filter(Imei=imei).filter(type_name=alarm_type).filter(date__range=[start_time, end_time])
    serializer = Alarmserializer(alarms, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def AlarmCreate(request):
    serializer = Alarmserializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



