from django.db import models

# Create your models here.
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class RelatedProduct(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='related_products')
    
    def __str__(self):
        return f'Related product for {self.product.name}'

class Product(models.Model):
    categories = models.ManyToManyField(Category)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    brewery = models.CharField(max_length=254)
    abv = models.DecimalField(max_digits=6, decimal_places=2)
    beer_type = models.CharField(max_length=254)
    description = models.TextField()
    volume = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    related_products_list = models.ForeignKey(RelatedProduct, on_delete=models.CASCADE, null=True, blank=True, related_name='related_products')

    def __str__(self):
        return self.name
