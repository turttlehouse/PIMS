# Generated by Django 5.0.2 on 2024-02-21 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0042_alter_doctor_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='profile_pic',
            field=models.ImageField(default=1, upload_to='profile_pic/DoctorProfilePic/'),
            preserve_default=False,
        ),
    ]
