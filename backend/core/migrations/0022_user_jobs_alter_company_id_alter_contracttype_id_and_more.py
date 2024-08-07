# Generated by Django 5.0.4 on 2024-08-07 13:50

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20220224_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='jobs',
            field=models.ManyToManyField(blank=True, null=True, related_name='users', to='core.job'),
        ),
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='contracttype',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='job',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='local',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='state',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='public_id',
            field=models.CharField(default=uuid.UUID('71b5c5a6-bef7-4427-b61e-a01ee89b0570'), help_text='Random sequence to be used as a public identifier.', max_length=255, unique=True),
        ),
        migrations.DeleteModel(
            name='UserJob',
        ),
    ]