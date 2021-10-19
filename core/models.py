from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=80)
    message = models.TextField(max_length=1000)

    created_at  = models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):
        return self.name


class HeaderImage(models.Model):
    image = models.ImageField(upload_to = 'header_image',default = 'IMG.JPG')

    