# Generated by Django 5.1.2 on 2024-10-11 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DadosHidricos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cidade', models.CharField(max_length=100)),
                ('ind_pluviometricos', models.DecimalField(decimal_places=4, max_digits=10)),
                ('bal_hidrico', models.DecimalField(decimal_places=4, max_digits=10)),
                ('precipitacao', models.DecimalField(decimal_places=4, max_digits=10)),
            ],
        ),
    ]
