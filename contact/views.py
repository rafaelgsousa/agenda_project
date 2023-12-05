from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def contact(request):
    return HttpResponse({'Hello World!'})

def page(request):
    return render(request, 'contact/index.html')