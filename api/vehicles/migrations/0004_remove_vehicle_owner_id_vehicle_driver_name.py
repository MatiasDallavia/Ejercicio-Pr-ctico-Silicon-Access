# Generated by Django 4.1 on 2024-03-23 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0003_rename_is_gone_vehicle_is_deleted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='owner_id',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='driver_name',
            field=models.CharField(default='vehicle', max_length=35),
            preserve_default=False,
        ),
    ]