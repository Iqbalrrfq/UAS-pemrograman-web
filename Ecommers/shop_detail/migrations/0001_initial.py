# Generated by Django 5.0 on 2023-12-31 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pembeli',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PESANAN', models.CharField(max_length=250)),
                ('JUMLAH_PESANAN', models.IntegerField(null=True)),
                ('HARGA', models.CharField(max_length=100)),
            ],
        ),
    ]