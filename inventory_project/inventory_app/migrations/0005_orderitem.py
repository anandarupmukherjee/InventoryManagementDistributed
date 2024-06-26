# Generated by Django 4.2.11 on 2024-04-01 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_app', '0004_itemwithdrawal'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=255)),
                ('supplier', models.CharField(max_length=255)),
                ('on_order', models.IntegerField(default=0)),
                ('quantity_per_unit', models.CharField(max_length=100)),
                ('unit', models.IntegerField()),
                ('minimum_unit', models.IntegerField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('request_date', models.CharField(max_length=255)),
                ('requested_by', models.CharField(max_length=255)),
                ('oracle_order_date', models.CharField(max_length=255)),
                ('oracle_po', models.CharField(max_length=255)),
                ('order_lead_time', models.CharField(max_length=255)),
            ],
        ),
    ]
