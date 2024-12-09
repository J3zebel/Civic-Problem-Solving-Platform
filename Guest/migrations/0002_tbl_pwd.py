# Generated by Django 5.1.3 on 2024-12-07 08:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0011_remove_tbl_localplace_district'),
        ('Guest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_pwd',
            fields=[
                ('pwd_id', models.TextField(editable=False, primary_key=True, serialize=False)),
                ('pwd_name', models.CharField(max_length=30)),
                ('pwd_email', models.CharField(max_length=40)),
                ('pwd_contact', models.CharField(max_length=30)),
                ('pwd_address', models.CharField(max_length=80)),
                ('pwd_proof', models.URLField()),
                ('pwd_password', models.CharField(max_length=30)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_district')),
            ],
        ),
    ]