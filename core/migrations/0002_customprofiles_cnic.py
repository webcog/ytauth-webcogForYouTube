# Generated by Django 5.0.6 on 2024-07-01 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customprofiles',
            name='cnic',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
