# Generated by Django 4.1 on 2023-07-03 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0011_homeblog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homeblog',
            options={'ordering': ['-date']},
        ),
    ]