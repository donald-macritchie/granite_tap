# Generated by Django 3.2.23 on 2024-01-04 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20240104_1619'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='origianl_bag',
            new_name='original_bag',
        ),
    ]