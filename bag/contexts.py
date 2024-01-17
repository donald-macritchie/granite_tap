from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def calculate_delivery_cost(bag_items):
    total_items = sum(item['quantity'] for item in bag_items)

    if total_items <= 4:
        return Decimal('3.50')
    else:
        total_cost = sum(item['quantity'] * item['product'].price for item in bag_items)
        
        if total_cost > settings.FREE_DELIVERY_THRESHOLD:
            return Decimal('0.00')
        else:
            return Decimal('4.50')

def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += item_data * product.price
        product_count += item_data
        bag_items.append({
            'item_id': item_id,
            'quantity': item_data,
            'product': product,
        })

    delivery = calculate_delivery_cost(bag_items)
    free_delivery_delta = max(settings.FREE_DELIVERY_THRESHOLD - total, Decimal('0'))

    grand_total = delivery + total if bag_items else Decimal('0.00')

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
