from django.contrib import admin
from .models import Pembeli

# Register your models here.

class MemberPembeli():
    list_display = ("PESANAN", "JUMLAH_PESANAN", "HARGA",)

admin.site.register(Pembeli)

