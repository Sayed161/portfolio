from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200,null=True)
    slug = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name


class Projects(models.Model):
    title = models.CharField(max_length=45)
    image = models.ImageField(upload_to='media/project/images/')
    video = models.FileField(upload_to='media/project/video')
    live_link = models.URLField(max_length=256)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.title
    
class Service(models.Model):
    image = models.ImageField(upload_to='media/',null=True)
    name = models.CharField(max_length=200,null=True)
    text = models.TextField()