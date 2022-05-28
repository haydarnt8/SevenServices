from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category (models.Model):
    cat_name= models.CharField(max_length=250)
    cat_image=models.ImageField(upload_to='Category_images/', blank=True)
    cat_details=models.TextField(null=True)

    def __str__(self):
        return f'{self.cat_name}'
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Service (models.Model):
    serv_name = models.CharField(max_length=250)
    serv_details=models.TextField()
    serv_Img = models.ImageField(upload_to='Service_images/', blank=True)
    date = models.DateTimeField(auto_now=True,null=True)
    # user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='x', blank=True)
    serv_cat=models.ForeignKey(Category,on_delete=models.CASCADE, related_name='y')

    def __str__(self):
        return f'{self.serv_name}'


    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


