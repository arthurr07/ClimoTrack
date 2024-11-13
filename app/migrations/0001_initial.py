# Generated by Django 5.1.2 on 2024-11-13 18:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.estado')),
            ],
        ),
        migrations.CreateModel(
            name='Precipitacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora', models.DecimalField(decimal_places=4, max_digits=10)),
                ('precipitacao', models.DecimalField(decimal_places=4, max_digits=10)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cidade')),
            ],
        ),
        migrations.CreateModel(
            name='DadosHidricos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pa_nivel_estacao_mb', models.DecimalField(decimal_places=4, max_digits=10)),
                ('pa_max_hora_mb', models.DecimalField(decimal_places=4, max_digits=10)),
                ('pa_min_hora_mb', models.DecimalField(decimal_places=4, max_digits=10)),
                ('radiacao_global_kjm2', models.DecimalField(decimal_places=4, max_digits=10)),
                ('temp_ar_bulbo_c', models.DecimalField(decimal_places=4, max_digits=10)),
                ('temp_orvalho_c', models.DecimalField(decimal_places=4, max_digits=10)),
                ('temp_max_hora_antes_c', models.DecimalField(decimal_places=4, max_digits=10)),
                ('temp_min_hora_antes_c', models.DecimalField(decimal_places=4, max_digits=10)),
                ('temp_orvalho_max_c', models.DecimalField(decimal_places=4, max_digits=10)),
                ('temp_orvalho_min_c', models.DecimalField(decimal_places=4, max_digits=10)),
                ('umid_rel_max_hora_per', models.DecimalField(decimal_places=4, max_digits=10)),
                ('umid_rel_min_hora_per', models.DecimalField(decimal_places=4, max_digits=10)),
                ('umid_rel_per', models.DecimalField(decimal_places=4, max_digits=10)),
                ('vento_direcao_gr', models.DecimalField(decimal_places=4, max_digits=10)),
                ('vento_rajada_ms', models.DecimalField(decimal_places=4, max_digits=10)),
                ('vento_velocidade_ms', models.DecimalField(decimal_places=4, max_digits=10)),
                ('precipitacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.precipitacao')),
            ],
        ),
    ]
