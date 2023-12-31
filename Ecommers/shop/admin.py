from django.contrib import admin 
from .models import Pembeli

# Register your models here.

class MemberPembeli():
    list_display = ("NAMA", "PESANAN", "JUMLAH_PESANAN",)

admin.site.register(Pembeli) 
