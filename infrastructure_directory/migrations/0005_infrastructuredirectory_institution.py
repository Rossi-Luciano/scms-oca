# Generated by Django 3.2.12 on 2022-08-15 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0003_institution_location'),
        ('infrastructure_directory', '0004_auto_20220809_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='infrastructuredirectory',
            name='institution',
            field=models.ManyToManyField(blank=True, to='institution.Institution'),
        ),
    ]
