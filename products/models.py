from django.db import models
from PIL import Image
import datetime
from django.contrib.auth.models import User
# Create your models here.


class Products(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default=None)
    picture = models.ImageField(upload_to='media')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    stock = models.PositiveIntegerField()
    date_added = models.DateField(default=datetime.datetime.now())
    category = models.ForeignKey('Categories', on_delete=models.PROTECT)

    # CATEGORIES = (
    #     ('ADS', 'ADIDASI'),
    #     ('TRC', 'TRICOURI'),
    #     ('PNT', 'PANTALONI'),
    #     ('TLF', 'TELEFOANE MOBILE'),
    #     ('ELCM', 'ELECTROCASNICE MARI'),
    # )
    # category = models.CharField(max_length=4, choices=CATEGORIES)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Products, self).save(*args, **kwargs)

        img = Image.open(self.picture.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.picture.path)


class Categories(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media')
    descriere = models.TextField(default=None)
    slug = models.CharField(max_length=50)

    def __str__(self):
        return self.name







