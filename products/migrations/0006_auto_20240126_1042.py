# Generated by Django 3.2.23 on 2024-01-26 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20240115_1325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='related_products_list',
        ),
        migrations.AlterField(
            model_name='product',
            name='brewery',
            field=models.CharField(max_length=252),
        ),
        migrations.DeleteModel(
            name='RelatedProduct',
        ),
    ]