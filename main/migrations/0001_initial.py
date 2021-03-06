# Generated by Django 3.2.3 on 2021-08-10 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('desc', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='department')),
            ],
            options={
                'verbose_name': 'department',
                'verbose_name_plural': 'departments',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Docter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('desc', models.CharField(max_length=500)),
                ('image', models.ImageField(blank=True, upload_to='docter')),
                ('qualification', models.CharField(max_length=100)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.department')),
            ],
            options={
                'verbose_name': 'Docter',
                'verbose_name_plural': 'Docters',
                'ordering': ('name',),
            },
        ),
    ]
