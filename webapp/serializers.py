from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from .models import myImageClass

class myImageClassSerializer(serializers.ModelSerializer):
    image = Base64ImageField()
    class Meta:
        model = myImageClass
        fields = ('data','image')

        def create(self, validated_data):
            image = validated_data.pop('image')
            data = validated_data.pop('data')
            return myImageClass.objects.create(data=data,   image=image)
