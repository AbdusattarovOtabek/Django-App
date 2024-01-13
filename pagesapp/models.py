from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


# Create your models here.

class Catalog(models.Model):
    name = models.CharField(max_length=200,)

    def get_absolute_url(self):
        return reverse('catalog', kwargs={'cat_id': self.pk})

    def __str__(self):
        return self.name

class Product(models.Model):
    cat = models.ForeignKey('Catalog',on_delete=models.CASCADE)
    product_name = models.CharField(max_length=250,verbose_name='Tovar')
    product_img = models.ImageField(upload_to='img/', blank=True,verbose_name='Rasm')
    product_info = models.CharField(max_length=300,verbose_name="Ma'lumotlar")
    product_price = models.IntegerField(verbose_name='Narxi')
    product_item = models.IntegerField(verbose_name='Soni')
    # create_time = models.DateTimeField(auto_now_add=True)
    # edit_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

