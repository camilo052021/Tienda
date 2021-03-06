# Generated by Django 4.0.1 on 2022-01-10 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=50, verbose_name='Producto')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('valor_unitario', models.FloatField(verbose_name='Precio')),
                ('valor', models.FloatField(verbose_name='Valor Compra')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.datos', verbose_name='Cliente')),
            ],
            options={
                'verbose_name': 'venta',
                'verbose_name_plural': 'ventas',
            },
        ),
    ]
