# Generated by Django 3.0.5 on 2020-04-18 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0016_asset_submission_model_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset_submission_model',
            name='approval_status',
            field=models.CharField(default='Pending', max_length=200),
        ),
    ]
