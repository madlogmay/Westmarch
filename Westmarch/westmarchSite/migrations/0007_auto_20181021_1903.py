# Generated by Django 2.1.2 on 2018-10-21 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('westmarchSite', '0006_towncrier_publishdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='towncrier',
            name='PublishDate',
            field=models.DateTimeField(),
        ),
    ]
