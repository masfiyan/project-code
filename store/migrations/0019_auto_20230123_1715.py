# Generated by Django 3.2.15 on 2023-01-23 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_alter_raw_material_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='raw_material',
            name='id1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='raw_material',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
