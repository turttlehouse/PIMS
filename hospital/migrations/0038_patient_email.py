# Generated by Django 5.0.2 on 2024-02-11 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0037_remove_patient_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
    ]