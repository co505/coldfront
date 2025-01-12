# Generated by Django 4.2.11 on 2025-01-12 23:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0004_auto_20230406_1133'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalproject',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical project', 'verbose_name_plural': 'historical projects'},
        ),
        migrations.AlterModelOptions(
            name='historicalprojectattribute',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical project attribute', 'verbose_name_plural': 'historical project attributes'},
        ),
        migrations.AlterModelOptions(
            name='historicalprojectattributetype',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical project attribute type', 'verbose_name_plural': 'historical project attribute types'},
        ),
        migrations.AlterModelOptions(
            name='historicalprojectattributeusage',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical project attribute usage', 'verbose_name_plural': 'historical project attribute usages'},
        ),
        migrations.AlterModelOptions(
            name='historicalprojectreview',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical project review', 'verbose_name_plural': 'historical project reviews'},
        ),
        migrations.AlterModelOptions(
            name='historicalprojectuser',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical project user', 'verbose_name_plural': 'historical Project User Status'},
        ),
        migrations.AlterField(
            model_name='historicalproject',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalprojectattribute',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalprojectattributetype',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalprojectattributeusage',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalprojectreview',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalprojectuser',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together={('title', 'pi')},
        ),
        migrations.CreateModel(
            name='ProjectInstitutionCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('institution', models.CharField(blank=True, max_length=4, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('project_code', models.CharField(blank=True, max_length=10, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]