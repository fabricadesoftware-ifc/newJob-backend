# Generated by Django 3.1.6 on 2021-02-19 16:48

import backend.files.models.document
import backend.files.models.image
from django.db import migrations, models
import secrets


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment_key', models.CharField(default=secrets.token_urlsafe, help_text='Used to attach the document to another object. Cannot be used to retrieve the document file.', max_length=255, unique=True)),
                ('public_id', models.CharField(default=secrets.token_urlsafe, help_text='Used to retrieve the document file itself. Should not be readable until the document is attached to another object.', max_length=255, unique=True)),
                ('file', models.FileField(upload_to=backend.files.models.document.document_file_path)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment_key', models.CharField(default=secrets.token_urlsafe, help_text='Used to attach the image to another object. Cannot be used to retrieve the image file.', max_length=255, unique=True)),
                ('public_id', models.CharField(default=secrets.token_urlsafe, help_text='Used to retrieve the image itself. Should not be readable until the image is attached to another object.', max_length=255, unique=True)),
                ('file', models.ImageField(upload_to=backend.files.models.image.image_file_path)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
