from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1023)
    skills = models.TextField(max_length=1023)
    thumbnail = models.ImageField(upload_to='project_thumbnails/')