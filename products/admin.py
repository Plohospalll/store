from django.contrib import admin

# Register your models here.
from products.models import ProductCotegory, Product

admin.site.register(ProductCotegory)
admin.site.register(Product)