# Generated by Django 4.0.4 on 2022-08-22 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0011_alter_profile_cgpa_alter_profile_clg_org_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Cgpa',
        ),
    ]
