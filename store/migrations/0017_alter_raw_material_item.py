# Generated by Django 3.2.15 on 2023-01-22 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_auto_20230122_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raw_material',
            name='item',
            field=models.TextField(),
        ),
    ]