# Generated by Django 5.0.4 on 2024-05-23 13:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0018_progresso_delete_progressoaluno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duvida',
            name='nome_treinador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.dados'),
        ),
    ]