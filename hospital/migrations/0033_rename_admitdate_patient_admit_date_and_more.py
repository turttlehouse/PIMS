# Generated by Django 5.0.2 on 2024-02-09 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0032_rename_admit_date_patient_admitdate_and_more'),
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
    ]
