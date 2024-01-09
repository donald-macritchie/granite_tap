from django.shortcuts import render, redirect, get_object_or_404
from .models import Wishlist
from products.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)

    template = 'wishlist/wishlist.html'

    context = {
        'wishlist_items': wishlist_items
    }

    return render(request, template, context)

