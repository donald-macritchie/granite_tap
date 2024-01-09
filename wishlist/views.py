from django.shortcuts import render, redirect, get_object_or_404
from .models import Wishlist
from products.models import Product
from django.contrib import messages

def wishlist(request):
    if request.user.is_authenticated:
        wishlist_item_ids = request.session.get('wishlist', [])
        wishlist_items = Product.objects.filter(pk__in=wishlist_item_ids)

        template = 'wishlist/wishlist.html'
        context = {
            'wishlist_items': wishlist_items,
        }
        return render(request, template, context)
    else:
        return redirect('product_detail')

def add_to_wishlist(request, item_id):
    """ Add a product to the wishlist """

    product = get_object_or_404(Product, pk=item_id)

    
    wishlist = request.session.get('wishlist', [])

    if item_id not in wishlist:
        wishlist.append(item_id)
        messages.success(request, f'Added {product.name} to your wishlist')
    else:
        messages.info(request, f'{product.name} is already in your wishlist.')

    request.session['wishlist'] = wishlist
    return redirect('product_detail', product_id=item_id)
