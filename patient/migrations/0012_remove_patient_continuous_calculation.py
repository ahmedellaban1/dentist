# Generated by Django 4.2.4 on 2023-08-31 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0011_alter_operation_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='continuous_calculation',
        ),
    ]
