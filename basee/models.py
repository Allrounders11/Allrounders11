from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NoteType(models.Model):
    name = models.CharField(max_length=300)

class Note(models.Model):
    type = models.ForeignKey(NoteType,on_delete=models.SET_NULL,null=True)
    