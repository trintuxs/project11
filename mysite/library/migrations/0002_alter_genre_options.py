# Generated by Django 4.2.1 on 2023-05-25 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': 'Žanras', 'verbose_name_plural': 'Žanrai'},
        ),
    ]