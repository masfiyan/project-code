# Generated by Django 3.2.15 on 2023-01-23 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_alter_raw_material_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raw_material',
            name='item',
            field=models.TextField(default=''),
        ),
    ]
