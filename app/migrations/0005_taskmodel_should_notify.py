# Generated by Django 4.2.23 on 2025-07-04 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_taskmodel_is_archived'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='should_notify',
            field=models.BooleanField(default=False),
        ),
    ]
