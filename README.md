# RestIAPIDjango
This repo consist of the rest API which uploads image using Base64 library and Django rest framework.

Here is how you can handle a Base64 encoded image file in a post request at the Django-based (drf also) API end which saves it as an ImageField.

First download the following library using following commands

~pip install django-extra-fields
~pip install pillow

#Let say you have a Model as follows:

Class MyImageModel(models.Model):
      image = models.ImageField(upload_to = 'geo_entity_pic')
      data=model.CharField()
      
#So the Corresponding Serializer would be as follows:

 from drf_extra_fields.fields import Base64ImageField

 Class MyImageModelSerializer(serializers.ModelSerializers):
      image=Base64ImageField()
      class meta:
         model=MyImageModel
         fields= ('data','image')
      def create(self, validated_data):
        image=validated_data.pop('image')
        data=validated_data.pop('data')
       return MyImageModel.objects.create(data=data,image=image)

#The corresponding View can be as follows:

elif request.method == 'POST':
    serializer = MyImageModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

#To run the server just create the super user and run command

~python manage.py runserver

-----------------------------------------------DONE----------------------------------------------------
