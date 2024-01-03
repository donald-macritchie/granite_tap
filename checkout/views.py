from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing in your bag at the moment.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OEY8hKJUkUZDiFC2r5zazrYvy4L2oKRJmViKK9QK2f5IB5UoPWZyDDUwHnsPAcdxvcYF5kSueoZs5utVk63nMF6006dhiS0hS',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)