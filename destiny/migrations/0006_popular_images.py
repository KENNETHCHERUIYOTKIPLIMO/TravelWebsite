# Generated by Django 3.2.23 on 2023-11-28 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destiny', '0005_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='popular',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
