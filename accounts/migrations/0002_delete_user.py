# Generated by Django 2.2.2 on 2019-08-30 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('posts', '0001_initial'),
        ('groups', '0002_auto_20190830_1210'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
