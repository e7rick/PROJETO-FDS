# Generated by Django 5.0.4 on 2024-05-06 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_rename_usuario_dados_nome'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgressoAluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_aluno', models.CharField(max_length=100)),
                ('metrica', models.CharField(max_length=100)),
                ('data', models.DateField()),
                ('progresso_observado', models.TextField()),
            ],
        ),
    ]
