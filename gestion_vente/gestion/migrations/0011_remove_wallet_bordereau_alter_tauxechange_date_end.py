# Generated by Django 5.2.1 on 2025-05-31 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0010_poste'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallet',
            name='bordereau',
        ),
        migrations.AlterField(
            model_name='tauxechange',
            name='date_end',
            field=models.DateTimeField(null=True),
        ),
    ]
