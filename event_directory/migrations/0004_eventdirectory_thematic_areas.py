# Generated by Django 3.2.12 on 2022-08-17 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usefulmodels', '0008_alter_thematicarea_options'),
        ('event_directory', '0003_alter_eventdirectory_attendence'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventdirectory',
            name='thematic_areas',
            field=models.ManyToManyField(blank=True, to='usefulmodels.ThematicArea'),
        ),
    ]
