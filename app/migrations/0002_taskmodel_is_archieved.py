# Generated by Django 4.2.23 on 2025-07-02 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='is_archieved',
            field=models.BooleanField(default=True),
        ),
    ]
