from rest_framework import serializers
from .models import AlarmTable


class Alarmserializer(serializers.ModelSerializer):
    """
    Serialize Order of Product
    """
    product = ProductField(queryset=Product.objects.all())

    class Meta:
        """
        Order metadata
        """
        model = AlarmTable
        fields = ('type_name', 'alarm_time', 'latitude', 'longitude')


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoUpload
        fields = ('id', 'file_list')
