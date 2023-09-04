# Generated by Django 4.2.4 on 2023-09-04 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0012_remove_patient_continuous_calculation'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='operation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='patient.operation'),
            preserve_default=False,
        ),
    ]
