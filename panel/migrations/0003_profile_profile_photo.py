# Generated by Django 4.0.4 on 2022-08-10 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0002_rename_projects_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
