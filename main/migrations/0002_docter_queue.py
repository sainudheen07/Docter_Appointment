# Generated by Django 3.2.3 on 2021-08-17 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='docter',
            name='queue',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
