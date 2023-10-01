# Generated by Django 4.2.5 on 2023-10-01 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extensionApi', '0007_alter_videodata_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videodata',
            name='videoId',
        ),
        migrations.AddField(
            model_name='videodata',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='videodata',
            name='video',
            field=models.FileField(upload_to='videos/'),
        ),
    ]
