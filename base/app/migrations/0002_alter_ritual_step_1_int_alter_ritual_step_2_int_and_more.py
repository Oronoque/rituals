# Generated by Django 4.2 on 2023-04-13 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ritual',
            name='step_1_int',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ritual',
            name='step_2_int',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ritual',
            name='step_3_int',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
