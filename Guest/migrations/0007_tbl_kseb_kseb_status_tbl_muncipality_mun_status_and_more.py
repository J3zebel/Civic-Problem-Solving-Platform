# Generated by Django 5.1.3 on 2024-12-12 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0006_tbl_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_kseb',
            name='kseb_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tbl_muncipality',
            name='mun_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tbl_mvd',
            name='mvd_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tbl_pwd',
            name='pwd_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tbl_user',
            name='user_status',
            field=models.IntegerField(default=0),
        ),
    ]
