from django.shortcuts import render

def index(request):
    context = {
        'judul':'Ecommers',
        'subjudul':'Selamat Datang',
    }
    return render(request,'index.html',context)