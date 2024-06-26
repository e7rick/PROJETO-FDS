# Generated by Django 5.0.4 on 2024-05-14 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_dica'),
    ]

    operations = [
        migrations.CreateModel(
            name='TreinoPredefinido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_treino', models.CharField(choices=[('costas', 'Costas'), ('peito', 'Peito'), ('perna', 'Perna'), ('braco', 'Braço')], max_length=20)),
                ('exercicio1_nome', models.CharField(max_length=100)),
                ('exercicio1_series', models.PositiveIntegerField()),
                ('exercicio1_repeticoes', models.PositiveIntegerField()),
                ('exercicio2_nome', models.CharField(max_length=100)),
                ('exercicio2_series', models.PositiveIntegerField()),
                ('exercicio2_repeticoes', models.PositiveIntegerField()),
                ('exercicio3_nome', models.CharField(max_length=100)),
                ('exercicio3_series', models.PositiveIntegerField()),
                ('exercicio3_repeticoes', models.PositiveIntegerField()),
                ('exercicio4_nome', models.CharField(max_length=100)),
                ('exercicio4_series', models.PositiveIntegerField()),
                ('exercicio4_repeticoes', models.PositiveIntegerField()),
            ],
        ),
    ]
