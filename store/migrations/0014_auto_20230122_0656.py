# Generated by Django 3.2.15 on 2023-01-22 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20230121_2108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='advance',
        ),
        migrations.RemoveField(
            model_name='order',
            name='remaining',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total',
        ),
    ]