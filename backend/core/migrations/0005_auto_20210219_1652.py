# Generated by Django 3.1.6 on 2021-02-19 16:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
        ('core', '0004_user_public_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='files.image'),
        ),
        migrations.AlterField(
            model_name='user',
            name='public_id',
            field=models.CharField(default=uuid.UUID('19b4dc59-bf51-4beb-966b-4d580dcd165e'), help_text='Random sequence to be used as a public identifier.', max_length=255, unique=True),
        ),
    ]
