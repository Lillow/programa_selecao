# Generated by Django 5.1.2 on 2024-10-21 21:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('containers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_movimentacao', models.CharField(choices=[('Embarque', 'Embarque'), ('Descarga', 'Descarga'), ('Gate In', 'Gate In'), ('Gate Out', 'Gate Out'), ('Reposicionamento', 'Reposicionamento'), ('Pesagem', 'Pesagem'), ('Scanner', 'Scanner')], max_length=20)),
                ('data_hora_inicio', models.DateTimeField()),
                ('data_hora_fim', models.DateTimeField()),
                ('container', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='containers.container')),
            ],
        ),
    ]
