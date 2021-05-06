# Generated by Django 3.2 on 2021-04-22 16:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=50)),
                ('customer_phone', models.CharField(max_length=15)),
                ('customer_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=50)),
                ('customer_phone', models.CharField(max_length=15)),
                ('products_dict', models.TextField(max_length=10000)),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('date', models.DateField(default=datetime.datetime.today)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('product_code', models.CharField(max_length=50)),
                ('unit_price', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('description', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('quantity', models.CharField(blank=True, max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='uploads/products/')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.category')),
            ],
        ),
    ]