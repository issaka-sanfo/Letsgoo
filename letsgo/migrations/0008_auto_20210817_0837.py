# Generated by Django 2.2.10 on 2021-08-17 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letsgo', '0007_auto_20210817_0835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accesstuto',
            old_name='date',
            new_name='access_date',
        ),
    ]
