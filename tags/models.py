from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=255) #max_length is a required field


class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE) #on_delete is a required
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) #on_delete is a required field
    object_id = models.PositiveIntegerField() #PositiveIntegerField is a required field 
    content_object = GenericForeignKey() #GenericForeignKey is a required field
    
