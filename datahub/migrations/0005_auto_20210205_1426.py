# Generated by Django 3.1.6 on 2021-02-05 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datahub', '0004_auto_20210203_1459'),
    ]

    operations = [
        migrations.RenameField(
            model_name='csv',
            old_name='activated',
            new_name='published',
        ),
    ]