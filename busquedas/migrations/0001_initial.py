# Generated by Django 3.2.6 on 2021-09-04 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Waste_Container',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=50)),
                ('deposit_content', models.CharField(max_length=1500)),
            ],
            options={
                'verbose_name': 'waste_container',
                'verbose_name_plural': 'wast_containers',
            },
        ),
        migrations.CreateModel(
            name='Solid_Waste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('recycle_type', models.CharField(max_length=1500)),
                ('material', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('waste_container', models.ManyToManyField(to='busquedas.Waste_Container')),
            ],
            options={
                'verbose_name': 'solid_waste',
                'verbose_name_plural': 'solid_wastes',
            },
        ),
    ]
