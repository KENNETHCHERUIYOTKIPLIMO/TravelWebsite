# Generated by Django 3.2.23 on 2023-11-28 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destiny', '0004_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=200)),
                ('travelDates', models.CharField(max_length=200)),
            ],
        ),
    ]
