# Generated by Django 4.2 on 2023-05-03 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('primera_aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contenido',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('phone', models.TextField()),
                ('last_name', models.TextField()),
                ('age', models.IntegerField()),
                ('email', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ContenidoProveedor',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('supplier_name', models.TextField()),
                ('phone', models.TextField()),
                ('email', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DatosCliente',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('direccion', models.TextField()),
                ('edad', models.IntegerField()),
                ('profesion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DatosProveedor',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('direccion', models.TextField()),
                ('area', models.TextField()),
                ('producto', models.TextField()),
            ],
        ),
    ]