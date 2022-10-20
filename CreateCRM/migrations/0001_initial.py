# Generated by Django 4.1.1 on 2022-10-20 20:18

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
            name='Create_CRM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateField()),
                ('descricao', models.TextField()),
                ('objetivo', models.TextField()),
                ('justificativa', models.TextField()),
                ('dependencia', models.BooleanField(default=False)),
                ('empresa', models.CharField(max_length=50)),
                ('status_crm', models.CharField(choices=[('Em processo', 'em processo'), ('Finalizadas', 'finalizadas'), ('Pendentes', 'pendentes')], max_length=50)),
                ('versao', models.IntegerField(default=1)),
                ('complexidade_crm', models.CharField(blank=True, choices=[('Alta', 'alta'), ('Media', 'media'), ('Baixa', 'baixa')], max_length=50)),
                ('file', models.FileField(blank=True, upload_to='files/%Y/%m/')),
                ('solicitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
