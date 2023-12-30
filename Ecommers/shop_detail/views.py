from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul':'Shop Detail',
    }
    return render(request, 'shop_detail/shop_detail.html',context)