from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul':'Shop',
    }
    return render(request, 'shop/shop.html',context)