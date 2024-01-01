from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul':'Contact',
    }
    return render(request, 'contact/contact.html',context)