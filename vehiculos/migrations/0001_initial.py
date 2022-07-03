# Generated by Django 4.0.5 on 2022-07-02 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='carros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
                ('cantidad_pasajeros', models.IntegerField()),
                ('fecha_salida', models.DateField()),
            ],
        ),
    ]
