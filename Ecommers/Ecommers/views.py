from django.shortcuts import render

def index(request):
    context = {
        'judul':'Ecommers',
    }
    return render(request,'index.html',context)