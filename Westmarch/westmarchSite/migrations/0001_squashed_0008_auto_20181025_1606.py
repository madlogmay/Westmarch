# Generated by Django 2.1.2 on 2018-11-03 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('westmarchSite', '0001_initial'), ('westmarchSite', '0002_remove_session_sessiondate'), ('westmarchSite', '0003_remove_towncryer_link'), ('westmarchSite', '0004_auto_20181013_1502'), ('westmarchSite', '0005_auto_20181013_1510'), ('westmarchSite', '0006_towncrier_publishdate'), ('westmarchSite', '0007_auto_20181021_1903'), ('westmarchSite', '0008_auto_20181025_1606')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CharName', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='CharItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CharID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='westmarchSite.Character')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='CityItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CityID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='westmarchSite.City')),
            ],
        ),
        migrations.CreateModel(
            name='GM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
                ('Description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=255)),
                ('SessionDate', models.DateTimeField()),
                ('RegionID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='westmarchSite.Region')),
            ],
        ),
        migrations.CreateModel(
            name='TownCrier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=128)),
                ('Description', models.TextField()),
                ('SessionID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='westmarchSite.Session', verbose_name='Game name')),
                ('PublishDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='World',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='region',
            name='WorldID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='westmarchSite.World'),
        ),
        migrations.AddField(
            model_name='cityitem',
            name='ItemID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='westmarchSite.Item'),
        ),
        migrations.AddField(
            model_name='city',
            name='RegionID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='westmarchSite.Region'),
        ),
        migrations.AddField(
            model_name='charitem',
            name='ItemID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='westmarchSite.Item'),
        ),
        migrations.RemoveField(
            model_name='session',
            name='SessionDate',
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
                ('GM', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='westmarchSite.GM')),
                ('Region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='westmarchSite.Region')),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='PlayerID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='westmarchSite.Player'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='PartyID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='westmarchSite.Party'),
            preserve_default=False,
        ),
    ]
