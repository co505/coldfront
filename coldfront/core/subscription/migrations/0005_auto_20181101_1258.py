# Generated by Django 2.1.2 on 2018-11-01 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0004_auto_20181101_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalsubscription',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]