# Generated by Django 5.1.3 on 2024-12-09 08:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0006_tbl_user'),
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_complaint',
            name='kseb',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_kseb'),
        ),
        migrations.AlterField(
            model_name='tbl_complaint',
            name='muncipality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_muncipality'),
        ),
        migrations.AlterField(
            model_name='tbl_complaint',
            name='mvd',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_mvd'),
        ),
        migrations.AlterField(
            model_name='tbl_complaint',
            name='pwd',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_pwd'),
        ),
    ]
