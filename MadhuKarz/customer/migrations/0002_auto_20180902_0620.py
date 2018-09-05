# Generated by Django 2.1.1 on 2018-09-02 06:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rental_Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_rent', models.FloatField()),
                ('insurance_cost', models.FloatField()),
                ('GST', models.FloatField()),
                ('total_amount_payable', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pick_location_id', models.CharField(max_length=50)),
                ('dropoff_location_id', models.CharField(max_length=20)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('remarks', models.CharField(max_length=300)),
                ('fuel_option_id', models.IntegerField()),
                ('rental_insurance_id', models.IntegerField()),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.Car', verbose_name='related car_id')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='related customer_id')),
            ],
        ),
        migrations.AddField(
            model_name='rental_invoice',
            name='rental_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.reservation', verbose_name='related rental_id'),
        ),
    ]
