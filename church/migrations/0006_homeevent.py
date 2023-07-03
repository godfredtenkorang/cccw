# Generated by Django 4.1 on 2023-07-02 19:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0005_delete_homeevent'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='home-event-img')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('organizer', models.CharField(max_length=50)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(default=django.utils.timezone.now)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('venue', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('slug', models.CharField(max_length=150)),
            ],
        ),
    ]