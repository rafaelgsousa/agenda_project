from django.shortcuts import redirect, render

from contact.forms import ContactForm


def create(request):
    if request.method == 'POST':
    #     first_name = request.POST.get("first_name", '').strip()
    #     last_name = request.POST.get("last_name", '').strip()

        # if first_name == '' | last_name == '':
        #     return redirect('contact:create')
        context = {
            'form': ContactForm(request.POST),
        }
        return render(
            request, 
            'contact/create.html', 
            context
            )
    context = {
            'form': ContactForm(),
        }
    return render(
            request, 
            'contact/create.html', 
            context
            )