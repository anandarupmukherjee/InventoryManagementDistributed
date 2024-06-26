# Generated by Django 4.2.11 on 2024-03-28 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=255)),
                ('supplier', models.CharField(max_length=255)),
                ('available', models.IntegerField()),
                ('quantity_per_unit', models.CharField(max_length=100)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
