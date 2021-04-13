# Generated by Django 3.1.6 on 2021-04-13 17:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210219_1655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='public_id',
            field=models.CharField(default=uuid.UUID('d33ebbea-6b16-4069-8d96-c5118278e2ab'), help_text='Random sequence to be used as a public identifier.', max_length=255, unique=True),
        ),
    ]