# Generated by Django 3.2.12 on 2022-10-22 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarly_articles', '0006_rawunpaywall_scholarly_a_is_para_720cbd_idx'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='contributors',
            index=models.Index(fields=['authenticated_orcid'], name='scholarly_a_authent_af2f9d_idx'),
        ),
        migrations.AddIndex(
            model_name='journals',
            index=models.Index(fields=['publisher'], name='scholarly_a_publish_e147df_idx'),
        ),
        migrations.AddIndex(
            model_name='journals',
            index=models.Index(fields=['journal_is_in_doaj'], name='scholarly_a_journal_cfb71a_idx'),
        ),
        migrations.AddIndex(
            model_name='rawunpaywall',
            index=models.Index(fields=['harvesting_creation'], name='scholarly_a_harvest_7bb154_idx'),
        ),
        migrations.AddIndex(
            model_name='rawunpaywall',
            index=models.Index(fields=['update'], name='scholarly_a_update_aaad1c_idx'),
        ),
        migrations.AddIndex(
            model_name='scholarlyarticles',
            index=models.Index(fields=['title'], name='scholarly_a_title_085dc7_idx'),
        ),
        migrations.AddIndex(
            model_name='scholarlyarticles',
            index=models.Index(fields=['volume'], name='scholarly_a_volume_9d7598_idx'),
        ),
        migrations.AddIndex(
            model_name='scholarlyarticles',
            index=models.Index(fields=['number'], name='scholarly_a_number_1341ed_idx'),
        ),
        migrations.AddIndex(
            model_name='scholarlyarticles',
            index=models.Index(fields=['year'], name='scholarly_a_year_1d73ef_idx'),
        ),
        migrations.AddIndex(
            model_name='scholarlyarticles',
            index=models.Index(fields=['open_access_status'], name='scholarly_a_open_ac_c69e94_idx'),
        ),
        migrations.AddIndex(
            model_name='scholarlyarticles',
            index=models.Index(fields=['use_license'], name='scholarly_a_use_lic_67590b_idx'),
        ),
        migrations.AddIndex(
            model_name='scholarlyarticles',
            index=models.Index(fields=['apc'], name='scholarly_a_apc_81f380_idx'),
        ),
        migrations.AddIndex(
            model_name='scholarlyarticles',
            index=models.Index(fields=['journal'], name='scholarly_a_journal_e944d8_idx'),
        ),
        migrations.AddIndex(
            model_name='scholarlyarticles',
            index=models.Index(fields=['source'], name='scholarly_a_source_6e535b_idx'),
        ),
    ]
