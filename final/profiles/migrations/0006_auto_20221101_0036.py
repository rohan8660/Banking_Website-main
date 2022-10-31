# Generated by Django 3.1.7 on 2022-10-31 19:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_remove_userinfo_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='id',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='password',
            field=models.CharField(default=datetime.datetime(2022, 10, 31, 19, 6, 48, 835877, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='mothers_name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
