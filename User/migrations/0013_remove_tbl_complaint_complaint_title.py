# Generated by Django 5.1.3 on 2025-02-08 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0012_tbl_request_kseb_tbl_request_mvd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_complaint',
            name='complaint_title',
        ),
    ]
