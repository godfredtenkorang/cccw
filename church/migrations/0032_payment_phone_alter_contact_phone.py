# Generated by Django 4.1 on 2023-09-10 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0031_merge_20230910_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='phone',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
