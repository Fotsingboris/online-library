# Generated by Django 4.0.5 on 2022-06-20 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_rename_adresse_store_addresse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='addresse',
        ),
        migrations.AlterField(
            model_name='store',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]