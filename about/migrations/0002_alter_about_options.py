# Generated by Django 3.2.23 on 2024-01-16 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'ordering': ['-title']},
        ),
    ]
