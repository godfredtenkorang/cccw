# Generated by Django 4.1 on 2023-07-11 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0030_payment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]