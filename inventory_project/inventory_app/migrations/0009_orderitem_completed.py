# Generated by Django 4.2.11 on 2024-04-02 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_app', '0008_alter_inventoryitem_oracle_order_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
