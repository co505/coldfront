# Generated by Django 3.2.13 on 2022-07-01 14:40

from django.db import migrations
import django.db.models.functions.text


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0002_auto_20191017_1141'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attributetype',
            options={'ordering': [django.db.models.functions.text.Lower('name')]},
        ),
        migrations.AlterModelOptions(
            name='resource',
            options={'ordering': [django.db.models.functions.text.Lower('name')]},
        ),
        migrations.AlterModelOptions(
            name='resourceattributetype',
            options={'ordering': [django.db.models.functions.text.Lower('name')]},
        ),
        migrations.AlterModelOptions(
            name='resourcetype',
            options={'ordering': [django.db.models.functions.text.Lower('name')]},
        ),
    ]
