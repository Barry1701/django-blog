from django.shortcuts import render
from .model import About

# Create your views here.

def about_me(request):
    """
    Render the About Page
    """
    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        'about/about.html',
        {'about':about},
    )
