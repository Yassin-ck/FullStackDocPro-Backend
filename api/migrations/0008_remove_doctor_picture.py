# Generated by Django 4.2.5 on 2023-09-11 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_doctor_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='picture',
        ),
    ]
