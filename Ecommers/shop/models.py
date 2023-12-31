from django.db import models

# Create your models here.

class Pembeli(models.Model):
    NAMA = models.CharField(max_length=100)
    PESANAN = models.CharField(max_length=250)
    JUMLAH_PESANAN = models.IntegerField(null=True)

    def _str_(self):
        return f"{self.NAMA}"