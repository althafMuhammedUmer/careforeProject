# Generated by Django 3.2.16 on 2023-03-18 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0006_alter_account_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address_line_1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
