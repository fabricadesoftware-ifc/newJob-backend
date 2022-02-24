# Generated by Django 3.1.6 on 2022-01-29 03:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20211103_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='public_id',
            field=models.CharField(default=uuid.UUID('58e20600-980d-4995-954e-69dda9447cac'), help_text='Random sequence to be used as a public identifier.', max_length=255, unique=True),
        ),
    ]