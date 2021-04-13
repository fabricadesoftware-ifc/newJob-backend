# Generated by Django 3.1.6 on 2021-02-19 16:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210219_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='public_id',
            field=models.CharField(default=uuid.UUID('f006a120-abd1-4153-aaa6-e28958f8d5b8'), help_text='Random sequence to be used as a public identifier.', max_length=255, unique=True),
        ),
    ]