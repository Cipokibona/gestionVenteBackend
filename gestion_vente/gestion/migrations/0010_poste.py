# Generated by Django 5.2.1 on 2025-05-31 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0009_vente_date_recouvrement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('salar', models.FloatField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
