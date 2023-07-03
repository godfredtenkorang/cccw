# Generated by Django 4.1 on 2023-07-03 07:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0012_alter_homeblog_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='home-blog-img')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', models.CharField(max_length=150)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]