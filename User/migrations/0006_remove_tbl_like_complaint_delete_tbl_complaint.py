# Generated by Django 5.1.3 on 2024-12-13 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MVD', '0002_remove_tbl_updates_complaint'),
        ('User', '0005_alter_tbl_complaint_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_like',
            name='complaint',
        ),
        migrations.DeleteModel(
            name='tbl_complaint',
        ),
    ]
