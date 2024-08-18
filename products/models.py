from django.db import models

# Create your models here.
class ProductCotegory(models.Model):
    name = models.CharField(max_length=100,unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=250,unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to=ProductCotegory,on_delete=models.CASCADE)

    def __str__(self):
        return f'Продукт:{self.name} | Категория:{self.category.name}'

