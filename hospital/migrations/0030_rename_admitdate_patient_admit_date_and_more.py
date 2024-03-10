# Generated by Django 5.0.2 on 2024-02-09 10:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0029_remove_doctor_email_hospitalstaffadmin_staff_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='admitDate',
            new_name='admit_date',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='assignedDoctorId',
            new_name='assigned_doctor_id',
        ),
        migrations.AddField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='first_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='last_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.CharField(max_length=100),
        ),
    ]