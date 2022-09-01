# Generated by Django 3.2.12 on 2022-08-29 09:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ThematicArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Data da última atualização')),
                ('level0', models.CharField(blank=True, choices=[('', ''), ('Ciências da Vida', 'Ciências da Vida'), ('Ciências Físicas, Tecnológicas e Multidisciplinares', 'Ciências Físicas, Tecnológicas e Multidisciplinares'), ('humanidades', 'Humanidades')], help_text='Here the thematic colleges of CAPES must be registered, more about these areas access: https://www.gov.br/capes/pt-br/acesso-a-informacao/acoes-e-programas/avaliacao/sobre-a-avaliacao/areas-avaliacao/sobre-as-areas-de-avaliacao/sobre-as-areas-de-avaliacao', max_length=255, null=True, verbose_name='Nível 0')),
                ('level1', models.CharField(blank=True, choices=[('', ''), ('Ciências Agrárias', 'Ciências Agrárias'), ('Ciências Biológicas', 'Ciências Biológicas'), ('Ciências da Saúde', 'Ciências da Saúde'), ('Ciências Exatas e da Terra', 'Ciências Exatas e da Terra'), ('Ciências Humanas', 'Ciências Humanas'), ('Ciências Sociais Aplicadas', 'Ciências Sociais Aplicadas'), ('Engenharias', 'Engenharias'), ('Lingüística, Letras e Artes', 'Lingüística, Letras e Artes')], help_text='Here the thematic colleges of CAPES must be registered, more about these areas access: https://www.gov.br/capes/pt-br/acesso-a-informacao/acoes-e-programas/avaliacao/sobre-a-avaliacao/areas-avaliacao/sobre-as-areas-de-avaliacao', max_length=255, null=True, verbose_name='Nível 1')),
                ('level2', models.CharField(blank=True, choices=[('', ''), ('Ciência de Alimentos', 'Ciência de Alimentos'), ('Ciências Agrárias I', 'Ciências Agrárias I'), ('Medicina Veterinária', 'Medicina Veterinária'), ('Zootecnia/Recursos Pesqueiros', 'Zootecnia/Recursos Pesqueiros'), ('Biodiversidade', 'Biodiversidade'), ('Ciências Biológicas I', 'Ciências Biológicas I'), ('Ciências Biológicas II', 'Ciências Biológicas II'), ('Ciências Biológicas III', 'Ciências Biológicas III'), ('Educação Física', 'Educação Física'), ('Enfermagem', 'Enfermagem'), ('Farmácia', 'Farmácia'), ('Medicina I', 'Medicina I'), ('Medicina II', 'Medicina II'), ('Medicina III', 'Medicina III'), ('Nutrição', 'Nutrição'), ('Odontologia', 'Odontologia'), ('Saúde Coletiva', 'Saúde Coletiva'), ('Astronomia/Física', 'Astronomia/Física'), ('Ciências da Computação', 'Ciências da Computação'), ('Geociências', 'Geociências'), ('Matemática/Probabilidade Estatística', 'Matemática/Probabilidade Estatística'), ('Química', 'Química'), ('Antropologia/Arqueologia', 'Antropologia/Arqueologia'), ('Ciência Política e Relações Internacionais', 'Ciência Política e Relações Internacionais'), ('Ciências da Religião e Teologia', 'Ciências da Religião e Teologia'), ('Educação', 'Educação'), ('Filosofia', 'Filosofia'), ('Geografia', 'Geografia'), ('História', 'História'), ('Psicologia', 'Psicologia'), ('Sociologia', 'Sociologia'), ('Turismo', 'Turismo'), ('Arquitetura, Urbanismo e Design', 'Arquitetura, Urbanismo e Design'), ('Comunicação e Informação', 'Comunicação e Informação'), ('Direito', 'Direito'), ('Economia', 'Economia'), ('Planejamento Urbano e Regional/Demografia', 'Planejamento Urbano e Regional/Demografia'), ('Serviço Social', 'Serviço Social'), ('Engenharias', 'Engenharias'), ('Engenharias I', 'Engenharias I'), ('Engenharias II', 'Engenharias II'), ('Engenharias III', 'Engenharias III'), ('Engenharias IV', 'Engenharias IV'), ('Artes', 'Artes'), ('Linguística e Literatura', 'Linguística e Literatura')], help_text='Here the thematic colleges of CAPES must be registered, more about these areas access: https://www.gov.br/capes/pt-br/acesso-a-informacao/acoes-e-programas/avaliacao/sobre-a-avaliacao/areas-avaliacao/sobre-as-areas-de-avaliacao', max_length=255, null=True, verbose_name='Nível 2')),
                ('creator', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='thematicarea_creator', to=settings.AUTH_USER_MODEL, verbose_name='Criador')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thematicarea_last_mod_user', to=settings.AUTH_USER_MODEL, verbose_name='Atualizador')),
            ],
            options={
                'verbose_name': 'Área temática',
                'verbose_name_plural': 'Áreas temáticas',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Data da última atualização')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nome do estado')),
                ('acronym', models.CharField(blank=True, max_length=255, null=True, verbose_name='Acrônimo do estado')),
                ('creator', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='state_creator', to=settings.AUTH_USER_MODEL, verbose_name='Criador')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='state_last_mod_user', to=settings.AUTH_USER_MODEL, verbose_name='Atualizador')),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
            },
        ),
        migrations.CreateModel(
            name='Practice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Data da última atualização')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name of the pratice')),
                ('code', models.CharField(blank=True, max_length=4, null=True, verbose_name='Code of the pratice')),
                ('creator', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='practice_creator', to=settings.AUTH_USER_MODEL, verbose_name='Criador')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='practice_last_mod_user', to=settings.AUTH_USER_MODEL, verbose_name='Atualizador')),
            ],
            options={
                'verbose_name': 'Practice',
                'verbose_name_plural': 'Practices',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Data da última atualização')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nome do País')),
                ('acronym', models.CharField(blank=True, max_length=255, null=True, verbose_name='Acrônimo do país')),
                ('creator', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='country_creator', to=settings.AUTH_USER_MODEL, verbose_name='Criador')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='country_last_mod_user', to=settings.AUTH_USER_MODEL, verbose_name='Atualizador')),
            ],
            options={
                'verbose_name': 'País',
                'verbose_name_plural': 'Países',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Data da última atualização')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nome da cidade')),
                ('creator', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='city_creator', to=settings.AUTH_USER_MODEL, verbose_name='Criador')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='city_last_mod_user', to=settings.AUTH_USER_MODEL, verbose_name='Atualizador')),
            ],
            options={
                'verbose_name': 'Cidade',
                'verbose_name_plural': 'Cidades',
            },
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Data da última atualização')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name of the action')),
                ('code', models.CharField(blank=True, max_length=4, null=True, verbose_name='Code of the action')),
                ('creator', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='action_creator', to=settings.AUTH_USER_MODEL, verbose_name='Criador')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='action_last_mod_user', to=settings.AUTH_USER_MODEL, verbose_name='Atualizador')),
            ],
            options={
                'verbose_name': 'Ação',
                'verbose_name_plural': 'Ações',
            },
        ),
    ]
