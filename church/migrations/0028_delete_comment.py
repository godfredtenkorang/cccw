# Generated by Django 4.1 on 2023-07-09 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0027_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]