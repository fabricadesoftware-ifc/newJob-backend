from django.contrib import admin

from backend.core.models import User, Company, Benefit, Category, Job, Local, State, City

admin.site.register(User)
admin.site.register(Company)
admin.site.register(Category)
admin.site.register(Job)
admin.site.register(Local)
admin.site.register(State)
admin.site.register(City)
