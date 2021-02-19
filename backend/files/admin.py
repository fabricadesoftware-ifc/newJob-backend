from django.contrib import admin

from backend.files.models import Image, Document

admin.site.register(Document)
admin.site.register(Image)