# Generated by Django 4.2.4 on 2023-08-28 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_prescription'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('amount_paid', models.IntegerField(default=0)),
                ('remaining_amount', models.IntegerField(default=0)),
                ('operation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.operation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
