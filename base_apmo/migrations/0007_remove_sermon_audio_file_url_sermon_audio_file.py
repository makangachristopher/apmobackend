# Generated by Django 5.1.4 on 2024-12-17 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_apmo', '0006_sermon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sermon',
            name='audio_file_url',
        ),
        migrations.AddField(
            model_name='sermon',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to='audio/sermons/', verbose_name='Audio File'),
        ),
    ]
