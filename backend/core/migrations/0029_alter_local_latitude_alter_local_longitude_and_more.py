# Generated by Django 5.1.1 on 2024-10-07 17:47

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_job_isexpired_alter_user_passage_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='local',
            name='latitude',
            field=models.DecimalField(decimal_places=4, max_digits=9),
        ),
        migrations.AlterField(
            model_name='local',
            name='longitude',
            field=models.DecimalField(decimal_places=4, max_digits=9),
        ),
        migrations.AlterField(
            model_name='user',
            name='passage_id',
            field=models.UUIDField(default=uuid.UUID('e3eaaea7-efcb-41c9-a00a-eec7983fd4a7'), help_text='Identificador de passagem', unique=True, verbose_name='ID de passagem'),
        ),
    ]
