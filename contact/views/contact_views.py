from django.http import HttpResponse
from django.shortcuts import render

from contact.models import Contact


# Create your views here.
def contact(request):
    return HttpResponse({'Hello World!'})

def page(request):
    return render(request, 'contact/index.html')

def index(request):
    contacts = Contact.objects.all()
    context = {
        'contacts': contacts
    }
    return render(request, 'contact/index.html', context)