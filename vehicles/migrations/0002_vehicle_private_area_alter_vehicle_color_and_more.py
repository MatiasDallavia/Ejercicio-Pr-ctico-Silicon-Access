# Generated by Django 4.1 on 2024-03-16 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='private_area',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.DO_NOTHING, to='users.privatearea'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='color',
            field=models.CharField(max_length=35),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='insurance',
            field=models.CharField(max_length=35),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='owner_id',
            field=models.BigIntegerField(),
        ),
    ]
