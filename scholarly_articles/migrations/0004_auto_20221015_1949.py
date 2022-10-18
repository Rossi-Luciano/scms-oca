# Generated by Django 3.2.12 on 2022-10-15 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarly_articles', '0003_auto_20221009_1418'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doi', models.CharField(max_length=100, verbose_name='DOI')),
                ('harvesting_creation', models.CharField(max_length=20, verbose_name='Data da coleta')),
                ('year', models.CharField(blank=True, max_length=10, null=True, verbose_name='Ano')),
                ('resource_type', models.CharField(blank=True, choices=[('', ''), ('book-section', 'Book Section'), ('monograph', 'Monograph'), ('report', 'Report'), ('peer-review', 'Peer Review'), ('book-track', 'Book Track'), ('journal-article', 'Journal Article'), ('book-part', 'Part'), ('other', 'Other'), ('book', 'Book'), ('journal-volume', 'Journal Volume'), ('book-set', 'Book Set'), ('reference-entry', 'Reference Entry'), ('proceedings-article', 'Proceedings Article'), ('journal', 'Journal'), ('component', 'Component'), ('book-chapter', 'Book Chapter'), ('proceedings-series', 'Proceedings Series'), ('report-series', 'Report Series'), ('proceedings', 'Proceedings'), ('standard', 'Standard'), ('reference-book', 'Reference Book'), ('posted-content', 'Posted Content'), ('journal-issue', 'Journal Issue'), ('dissertation', 'Dissertation'), ('grant', 'Grant'), ('dataset', 'Dataset'), ('book-series', 'Book Series'), ('edited-book', 'Edited Book'), ('standard-series', 'Standard Series')], max_length=50, verbose_name='Tipo de recurso')),
                ('source', models.CharField(max_length=100, verbose_name='Origem')),
                ('json', models.JSONField(blank=True, null=True, verbose_name='Arquivo JSON')),
            ],
        ),
        migrations.DeleteModel(
            name='RawUnpaywall',
        ),
        migrations.DeleteModel(
            name='SupplementaryData',
        ),
        migrations.AddIndex(
            model_name='rawrecord',
            index=models.Index(fields=['doi'], name='scholarly_a_doi_09885f_idx'),
        ),
        migrations.AddIndex(
            model_name='rawrecord',
            index=models.Index(fields=['year'], name='scholarly_a_year_6cceb5_idx'),
        ),
        migrations.AddIndex(
            model_name='rawrecord',
            index=models.Index(fields=['resource_type'], name='scholarly_a_resourc_3328e4_idx'),
        ),
    ]
