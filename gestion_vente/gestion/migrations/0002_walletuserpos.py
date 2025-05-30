# Generated by Django 5.2.1 on 2025-05-27 06:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WalletUserPos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.FloatField()),
                ('is_active', models.BooleanField(default=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='panier_user', to='gestion.basketagent')),
                ('typeEchange', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type_echange', to='gestion.typeechange')),
            ],
        ),
    ]
