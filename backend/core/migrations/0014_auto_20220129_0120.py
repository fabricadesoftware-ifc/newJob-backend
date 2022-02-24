# Generated by Django 3.1.6 on 2022-01-29 04:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20220129_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='public_id',
            field=models.CharField(default=uuid.UUID('897f9be5-ac7f-48d0-ad6b-7b7ae25feb4d'), help_text='Random sequence to be used as a public identifier.', max_length=255, unique=True),
        ),
    ]