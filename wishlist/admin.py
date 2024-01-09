from django.contrib import admin
from .models import Wishlist

class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'display_product', 'date_added')

    def display_product(self, obj):
        return obj.product.name

admin.site.register(Wishlist, WishlistAdmin)