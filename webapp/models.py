from django.db import models

# Create your models here.

class myImageClass(models.Model):
    image = models.ImageField(upload_to = 'geo_entity_pic')
    data = models.CharField(max_length=10)

    def __str__(self):
        return self.image

    def __str__(self):
        return self.data    