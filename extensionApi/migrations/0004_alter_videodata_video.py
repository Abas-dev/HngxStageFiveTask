# Generated by Django 4.2.5 on 2023-09-30 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extensionApi', '0003_alter_videodata_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videodata',
            name='video',
            field=models.FileField(upload_to='video/'),
        ),
    ]