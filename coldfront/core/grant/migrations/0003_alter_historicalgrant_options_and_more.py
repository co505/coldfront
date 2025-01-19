# Generated by Django 4.2.11 on 2025-01-19 19:54

import coldfront.core.grant.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grant', '0002_auto_20230406_1310'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalgrant',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical grant', 'verbose_name_plural': 'historical Grants'},
        ),
        migrations.AlterField(
            model_name='grant',
            name='direct_funding',
            field=coldfront.core.grant.models.MoneyField(max_length=100),
        ),
        migrations.AlterField(
            model_name='grant',
            name='percent_credit',
            field=coldfront.core.grant.models.PercentField(max_length=100, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='grant',
            name='total_amount_awarded',
            field=coldfront.core.grant.models.MoneyField(max_length=100),
        ),
        migrations.AlterField(
            model_name='historicalgrant',
            name='direct_funding',
            field=coldfront.core.grant.models.MoneyField(max_length=100),
        ),
        migrations.AlterField(
            model_name='historicalgrant',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalgrant',
            name='percent_credit',
            field=coldfront.core.grant.models.PercentField(max_length=100, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='historicalgrant',
            name='total_amount_awarded',
            field=coldfront.core.grant.models.MoneyField(max_length=100),
        ),
    ]
