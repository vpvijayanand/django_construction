# Generated by Django 5.1.3 on 2024-11-18 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Brand Name')),
                ('mobile1', models.CharField(blank=True, max_length=15, null=True, verbose_name='Mobile 1')),
                ('mobile2', models.CharField(blank=True, max_length=15, null=True, verbose_name='Mobile 2')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
        ),
    ]
