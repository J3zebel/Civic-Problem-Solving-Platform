# Generated by Django 5.1.3 on 2024-12-20 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0010_tbl_request'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_request',
            name='kseb',
        ),
        migrations.RemoveField(
            model_name='tbl_request',
            name='mvd',
        ),
    ]
