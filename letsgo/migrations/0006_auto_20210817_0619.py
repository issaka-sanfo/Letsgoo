# Generated by Django 2.2.10 on 2021-08-17 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letsgo', '0005_auto_20210817_0459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchage',
            name='activated',
            field=models.BooleanField(default=True),
        ),
    ]