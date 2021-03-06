# Generated by Django 3.2 on 2021-11-23 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(blank=True, null=True)),
                ('customer', models.TextField(blank=True, null=True)),
                ('products', models.TextField(max_length=255)),
                ('product_description', models.TextField(blank=True, null=True)),
                ('paymentMethod', models.CharField(blank=True, max_length=225, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('total', models.TextField(blank=True, null=True)),
                ('shop_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.shop')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CheckedOut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.TextField(blank=True, null=True)),
                ('product_name', models.CharField(max_length=255)),
                ('product_description', models.TextField(blank=True, null=True)),
                ('product_model', models.CharField(blank=True, max_length=255, null=True)),
                ('product_part_number', models.CharField(blank=True, max_length=255, null=True)),
                ('product_price', models.CharField(max_length=255)),
                ('product_promote', models.BooleanField(blank=True, default=False, null=True)),
                ('product_promotion', models.CharField(blank=True, max_length=255, null=True)),
                ('product_size', models.CharField(blank=True, max_length=225, null=True)),
                ('product_quantity', models.IntegerField(default=1)),
                ('product_creation_date', models.DateField(auto_now_add=True)),
                ('product_specifications', models.TextField(blank=True, null=True)),
                ('product_last_price', models.CharField(blank=True, max_length=225, null=True)),
                ('product_buying_price', models.CharField(blank=True, max_length=225, null=True)),
                ('shop_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.shop')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
