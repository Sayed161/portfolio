from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    image = models.ImageField(upload_to='media/images/')