# Generated by Django 3.0.5 on 2020-04-13 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assets', '0006_delete_asset_submission'),
    ]

    operations = [
        migrations.CreateModel(
            name='asset_submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=200)),
                ('lname', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('assets', models.CharField(max_length=200)),
                ('manager', models.CharField(max_length=200)),
            ],
        ),
    ]
