# Generated by Django 3.0.5 on 2020-04-15 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0013_auto_20200415_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset_submission_model',
            name='username',
            field=models.CharField(default='', max_length=200),
        ),
    ]
