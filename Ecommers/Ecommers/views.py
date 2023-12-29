from django.shortcuts import render

def index(request):
    context = {
        'judul':'BuahSayuran',
    }
    return render(request,'index.html',context)