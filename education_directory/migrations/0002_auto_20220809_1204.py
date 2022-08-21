# Generated by Django 3.2.12 on 2022-08-09 12:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtaildocs', '0012_uploadeddocument'),
        ('education_directory', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='educationdirectory',
            options={'verbose_name_plural': 'Diretório de Educação'},
        ),
        migrations.AlterModelOptions(
            name='educationdirectoryfile',
            options={'verbose_name_plural': 'Diretório de Educação Upload'},
        ),
        migrations.AlterField(
            model_name='educationdirectory',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data de criação'),
        ),
        migrations.AlterField(
            model_name='educationdirectory',
            name='creator',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='educationdirectory_creator', to=settings.AUTH_USER_MODEL, verbose_name='Criador'),
        ),
        migrations.AlterField(
            model_name='educationdirectory',
            name='description',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='educationdirectory',
            name='end_date',
            field=models.DateField(blank=True, max_length=255, null=True, verbose_name='Data de fim'),
        ),
        migrations.AlterField(
            model_name='educationdirectory',
            name='end_time',
            field=models.TimeField(blank=True, max_length=255, null=True, verbose_name='Hora final'),
        ),
        migrations.AlterField(
            model_name='educationdirectory',
            name='institution',
            field=models.TextField(max_length=255, verbose_name='Instituição'),
        ),
        migrations.AlterField(
            model_name='educationdirectory',
            name='start_date',
            field=models.DateField(blank=True, max_length=255, null=True, verbose_name='Data de início'),
        ),
        migrations.AlterField(
            model_name='educationdirectory',
            name='start_time',
            field=models.TimeField(blank=True, max_length=255, null=True, verbose_name='Hora inicial'),
        ),
        migrations.AlterField(
            model_name='educationdirectory',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Data da última atualização'),
        ),
        migrations.AlterField(
            model_name='educationdirectory',
            name='updated_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='educationdirectory_last_mod_user', to=settings.AUTH_USER_MODEL, verbose_name='Atualizador'),
        ),
        migrations.AlterField(
            model_name='educationdirectoryfile',
            name='attachment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document', verbose_name='Anexo'),
        ),
        migrations.AlterField(
            model_name='educationdirectoryfile',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data de criação'),
        ),
        migrations.AlterField(
            model_name='educationdirectoryfile',
            name='creator',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='educationdirectoryfile_creator', to=settings.AUTH_USER_MODEL, verbose_name='Criador'),
        ),
        migrations.AlterField(
            model_name='educationdirectoryfile',
            name='is_valid',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='É válido'),
        ),
        migrations.AlterField(
            model_name='educationdirectoryfile',
            name='line_count',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Número de linhas'),
        ),
        migrations.AlterField(
            model_name='educationdirectoryfile',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Data da última atualização'),
        ),
        migrations.AlterField(
            model_name='educationdirectoryfile',
            name='updated_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='educationdirectoryfile_last_mod_user', to=settings.AUTH_USER_MODEL, verbose_name='Atualizador'),
        ),
    ]
