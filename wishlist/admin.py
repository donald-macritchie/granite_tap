from django.contrib import admin
from .models import Wishlist


class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'display_product', 'date_added')

    def display_product(self, obj):
        return ', '.join([product.name for product in obj.products.all()])

    display_product.short_description = 'Products'


admin.site.register(Wishlist, WishlistAdmin)
