from django.shortcuts import render
from .models import About, FAQ

def about_page(request):
    about_content = About.objects.first()
    faqs = FAQ.objects.all()

    content {
        'about_content': about_content,
        'faqs': faqs,
    }
    return render(request, 'pages/about.html', )