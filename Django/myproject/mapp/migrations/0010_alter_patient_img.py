# Generated by Django 4.2 on 2023-05-01 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapp', '0009_alter_patient_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='img',
            field=models.ImageField(upload_to='media/'),
        ),
    ]