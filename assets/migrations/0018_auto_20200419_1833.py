# Generated by Django 3.0.5 on 2020-04-19 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0017_auto_20200418_1827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset_submission_model',
            name='manager',
        ),
        migrations.AddField(
            model_name='asset_submission_model',
            name='manager_email',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='asset_submission_model',
            name='manager_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
