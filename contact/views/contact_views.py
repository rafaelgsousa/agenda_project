from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from contact.models import Contact


# Create your views here.
def hello(request):
    return HttpResponse({'Hello World!'})

def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')
    # print(contacts.query)
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        "site_title": "Contatos - "
    }
    return render(request, 'contact/index.html', context)

def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')
    
    contacts = Contact.objects\
            .filter(show=True)\
            .filter(
                Q(first_name__icontains=search_value) |
                Q(last_name__icontains=search_value)|
                Q(email__icontains=search_value) |
                Q(phone__icontains=search_value) 
                )\
            .order_by('-id')
    
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        "site_title": "Search - "
    }
    return render(request, 'contact/index.html', context)

def contact(request, contact_id):
    # single_contact = Contact.objects.filter(pk=contact_id).first()
    single_contact = get_object_or_404(Contact.objects.filter(pk=contact_id, show=True))
    # if single_contact is None:
    #     raise Http404('Contact not found')
    contact_name = f'{single_contact.first_name} {single_contact.last_name}'
    context = {
        'contact': single_contact,
        'site_title': f'{contact_name} - '
    }
    return render(request, 'contact/contact.html', context)