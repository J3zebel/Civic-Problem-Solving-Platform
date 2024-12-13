# Generated by Django 5.1.3 on 2024-12-13 08:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0007_tbl_kseb_kseb_status_tbl_muncipality_mun_status_and_more'),
        ('User', '0003_tbl_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.tbl_complaint')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]