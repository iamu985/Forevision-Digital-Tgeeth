# Generated by Django 4.1.3 on 2023-01-25 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clip',
            name='audio_file',
            field=models.FileField(upload_to='resources/'),
        ),
    ]