# Generated by Django 4.2 on 2023-04-13 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_ritual_step_1_int_alter_ritual_step_2_int_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ritual',
            name='is_step_1_complete',
        ),
        migrations.RemoveField(
            model_name='ritual',
            name='is_step_2_complete',
        ),
        migrations.RemoveField(
            model_name='ritual',
            name='is_step_3_complete',
        ),
        migrations.RemoveField(
            model_name='ritual',
            name='step_1',
        ),
        migrations.RemoveField(
            model_name='ritual',
            name='step_1_int',
        ),
        migrations.RemoveField(
            model_name='ritual',
            name='step_1_unit',
        ),
        migrations.RemoveField(
            model_name='ritual',
            name='step_2',
        ),
        migrations.RemoveField(
            model_name='ritual',
            name='step_2_int',
        ),
        migrations.RemoveField(
            model_name='ritual',
            name='step_2_unit',
        ),
        migrations.RemoveField(
            model_name='ritual',
            name='step_3',
        ),
        migrations.RemoveField(
            model_name='ritual',
            name='step_3_int',
        ),
        migrations.RemoveField(
            model_name='ritual',
            name='step_3_unit',
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('value', models.FloatField(blank=True, null=True)),
                ('unit', models.CharField(blank=True, choices=[('miles', 'Miles'), ('reps', 'Reps'), ('lbs', 'Lbs'), ('minute', 'Minutes')], max_length=10, null=True)),
                ('is_complete', models.BooleanField(default=False)),
                ('ritual', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='app.ritual')),
            ],
        ),
    ]
