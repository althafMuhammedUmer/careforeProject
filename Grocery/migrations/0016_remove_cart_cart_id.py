# Generated by Django 4.1.1 on 2022-10-08 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Grocery', '0015_cartitem_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='cart_id',
        ),
    ]