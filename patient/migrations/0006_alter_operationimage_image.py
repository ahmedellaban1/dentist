# Generated by Django 4.2.4 on 2023-08-28 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0005_alter_operationimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operationimage',
            name='image',
            field=models.ImageField(upload_to='2167307735-'),
        ),
    ]
