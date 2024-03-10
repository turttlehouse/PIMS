# Generated by Django 5.0.2 on 2024-02-25 06:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0046_alter_doctor_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance_provider', models.CharField(blank=True, max_length=100)),
                ('policy_number', models.CharField(blank=True, max_length=100)),
                ('group_number', models.CharField(blank=True, max_length=100)),
                ('effective_date', models.DateField(blank=True, null=True)),
                ('expiration_date', models.DateField(blank=True, null=True)),
                ('copayment_info', models.CharField(blank=True, max_length=100)),
                ('status', models.BooleanField(default=True)),
                ('patient', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.patient')),
            ],
        ),
    ]