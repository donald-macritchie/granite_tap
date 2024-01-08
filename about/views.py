from django.shortcuts import render
from .models import About, FAQ

def about_page(request):
    about_content = About.objects.all()
    faqs = FAQ.objects.all()

    template = 'about/about.html'

    context = {
        'about_content': about_content,
        'faqs': faqs,
    }
    return render(request, template, context)