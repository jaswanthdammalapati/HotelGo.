# Generated by Django 5.0.1 on 2024-01-14 16:52

import datetime
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('image1', models.ImageField(upload_to='images/hotel_images/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='images/hotel_images/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='images/hotel_images/')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='images/hotel_images/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('free_wifi', models.BooleanField(default=False)),
                ('fitness_center', models.BooleanField(default=False)),
                ('breakfast', models.BooleanField(default=False)),
                ('swimming_pool', models.BooleanField(default=False)),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('capacity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='RoomReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('guest_name', models.CharField(max_length=255)),
                ('guest_email', models.EmailField(max_length=254)),
                ('guest_phone', models.CharField(max_length=15)),
                ('checkin_date', models.DateField(default=datetime.datetime.now)),
                ('checkout_date', models.DateField(default=datetime.datetime.now)),
                ('booked_on', models.DateTimeField(auto_now_add=True)),
                ('num_days', models.PositiveIntegerField(default=1)),
                ('cost', models.PositiveIntegerField()),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.hotel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.roomtype')),
            ],
        ),
        migrations.CreateModel(
            name='HotelRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_rooms', models.PositiveIntegerField(default=0)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.hotel')),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.roomtype')),
            ],
        ),
        migrations.AddField(
            model_name='hotel',
            name='room_types',
            field=models.ManyToManyField(through='hotels.HotelRoom', to='hotels.roomtype'),
        ),
    ]