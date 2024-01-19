from django.shortcuts import render, redirect
from django.contrib import messages
from .models import About, FAQ, Contact
from .forms import ContactForm

def about_page(request):
    about_content = About.objects.all()
    faqs = FAQ.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
            return redirect('about_page')
        else:
            messages.error(request, 'There was an error with your submission. Please check the form.')

    else:
        form = ContactForm()

    template = 'about/about.html'

    context = {
        'about_content': about_content,
        'faqs': faqs,
        'contact_form': form,
        'contact_info': Contact.objects.first(),  # Assuming you have only one contact entry
    }
    return render(request, template, context)
