# Generated by Django 3.1.5 on 2021-01-23 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210123_1132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clinicprofile',
            old_name='image',
            new_name='avatar',
        ),
    ]
